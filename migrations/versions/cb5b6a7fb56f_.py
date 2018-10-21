"""empty message

Revision ID: cb5b6a7fb56f
Revises: 8fc027b37577
Create Date: 2018-02-23 10:59:57.377000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cb5b6a7fb56f'
down_revision = '8fc027b37577'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('new_feature1', sa.Integer(), nullable=True))
    op.drop_column('article', 'new_feature')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('new_feature', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('article', 'new_feature1')
    # ### end Alembic commands ###
