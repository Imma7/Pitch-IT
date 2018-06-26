"""Initial Migration

Revision ID: 84a9417f9dda
Revises: 0a2184f29aee
Create Date: 2018-06-26 10:50:52.388471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84a9417f9dda'
down_revision = '0a2184f29aee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'email')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
