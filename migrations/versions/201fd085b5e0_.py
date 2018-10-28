"""empty message

Revision ID: 201fd085b5e0
Revises: cb5b6a7fb56f
Create Date: 2018-02-23 11:03:54.729000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '201fd085b5e0'
down_revision = 'cb5b6a7fb56f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('new_feature2', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'new_feature2')
    # ### end Alembic commands ###