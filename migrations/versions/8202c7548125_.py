"""empty message

Revision ID: 8202c7548125
Revises: 
Create Date: 2017-08-12 00:32:35.615330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8202c7548125'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('telephone', sa.String(length=11), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
