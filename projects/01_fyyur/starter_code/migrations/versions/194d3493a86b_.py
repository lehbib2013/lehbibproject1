"""empty message

Revision ID: 194d3493a86b
Revises: d63a34d5d17c
Create Date: 2021-12-02 23:45:28.566153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '194d3493a86b'
down_revision = 'd63a34d5d17c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('availablities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('available_time', sa.DateTime(), nullable=False),
    sa.Column('booked', sa.Boolean(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('availablities')
    # ### end Alembic commands ###
