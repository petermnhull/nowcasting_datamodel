"""Add model_id to forecast_value_latest

Found to run this migration I have to set nullable=True and then run

update forecast_value_latest
set model_id=-1
This took ~3 minutes.

Then you might need too
run this

alter table forecast_value_latest
drop constraint forecast_value_latest_pkey;

alter table forecast_value_latest
add constraint forecast_value_latest_pkey primary key (target_time, gsp_id, model_id);

Revision ID: 489955d7a5a0
Revises: 09f38fe306a4
Create Date: 2023-04-05 12:10:16.432811

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "489955d7a5a0"
down_revision = "09f38fe306a4"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("forecast_value_latest", sa.Column("model_id", sa.Integer(), nullable=False))
    op.drop_index("uix_1", table_name="forecast_value_latest")
    op.create_index(
        "uix_1",
        "forecast_value_latest",
        ["gsp_id", "target_time", "model_id"],
        unique=True,
        postgresql_where=sa.text("is_primary"),
    )
    op.create_index(
        op.f("ix_forecast_value_latest_model_id"),
        "forecast_value_latest",
        ["model_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_forecast_value_latest_model_id"), table_name="forecast_value_latest")
    op.drop_index(
        "uix_1", table_name="forecast_value_latest", postgresql_where=sa.text("is_primary")
    )
    op.create_index("uix_1", "forecast_value_latest", ["gsp_id", "target_time"], unique=False)
    op.drop_column("forecast_value_latest", "model_id")
    # ### end Alembic commands ###
