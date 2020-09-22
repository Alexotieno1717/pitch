"""image migration

Revision ID: 352cec81d735
Revises: 6fe91df40dcd
Create Date: 2020-09-22 12:08:23.740141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '352cec81d735'
down_revision = '6fe91df40dcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('writer', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['writer'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'writer')
    # ### end Alembic commands ###