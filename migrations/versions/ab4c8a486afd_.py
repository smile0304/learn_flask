"""empty message

Revision ID: ab4c8a486afd
Revises: 8ea2da877e3d
Create Date: 2017-08-13 02:03:08.602830

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ab4c8a486afd'
down_revision = '8ea2da877e3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('author_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'answer_ibfk_1', 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'user', ['author_id'], ['id'])
    op.drop_column('answer', 'authore_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('authore_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.create_foreign_key(u'answer_ibfk_1', 'answer', 'user', ['authore_id'], ['id'])
    op.drop_column('answer', 'author_id')
    # ### end Alembic commands ###