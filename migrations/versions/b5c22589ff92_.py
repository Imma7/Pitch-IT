"""empty message

Revision ID: b5c22589ff92
Revises: bbfc9186d81c
Create Date: 2018-07-02 19:44:21.556644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5c22589ff92'
down_revision = 'bbfc9186d81c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('name', sa.String(), nullable=True))
    op.drop_column('categories', 'category_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('category_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('categories', 'name')
    # ### end Alembic commands ###
