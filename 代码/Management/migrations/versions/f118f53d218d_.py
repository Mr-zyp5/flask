"""empty message

Revision ID: f118f53d218d
Revises: ed7a0c0ff82b
Create Date: 2020-03-16 19:33:38.765298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f118f53d218d'
down_revision = 'ed7a0c0ff82b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notice', sa.Column('author', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notice', 'author')
    # ### end Alembic commands ###
