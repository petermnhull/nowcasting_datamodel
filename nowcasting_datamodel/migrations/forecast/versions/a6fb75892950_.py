"""Add properties column to forecast_value

Revision ID: a6fb75892950
Revises: 08ba6879b865
Create Date: 2023-07-03 11:00:31.216789

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a6fb75892950"
down_revision = "08ba6879b865"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column("forecast_value", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2022_09", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2022_10", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2022_11", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2022_12", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_01", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_02", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_03", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_04", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_05", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_06", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_07", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_08", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_09", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_10", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_11", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_2023_12", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column(
        "forecast_value_last_seven_days", sa.Column("properties", sa.JSON(), nullable=True)
    )
    op.add_column("forecast_value_latest", sa.Column("properties", sa.JSON(), nullable=True))
    op.add_column("forecast_value_old", sa.Column("properties", sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("forecast_value_old", "properties")
    op.drop_column("forecast_value_latest", "properties")
    op.drop_column("forecast_value_last_seven_days", "properties")
    op.drop_column("forecast_value_2023_12", "properties")
    op.drop_column("forecast_value_2023_11", "properties")
    op.drop_column("forecast_value_2023_10", "properties")
    op.drop_column("forecast_value_2023_09", "properties")
    op.drop_column("forecast_value_2023_08", "properties")
    op.drop_column("forecast_value_2023_07", "properties")
    op.drop_column("forecast_value_2023_06", "properties")
    op.drop_column("forecast_value_2023_05", "properties")
    op.drop_column("forecast_value_2023_04", "properties")
    op.drop_column("forecast_value_2023_03", "properties")
    op.drop_column("forecast_value_2023_02", "properties")
    op.drop_column("forecast_value_2023_01", "properties")
    op.drop_column("forecast_value_2022_12", "properties")
    op.drop_column("forecast_value_2022_11", "properties")
    op.drop_column("forecast_value_2022_10", "properties")
    op.drop_column("forecast_value_2022_09", "properties")
    op.drop_column("forecast_value", "properties")

    # ### end Alembic commands ###
