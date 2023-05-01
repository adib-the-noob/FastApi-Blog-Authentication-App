"""empty message

Revision ID: 2dd28742b03b
Revises: c3490ae2d59c
Create Date: 2023-05-01 03:09:48.742224

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2dd28742b03b'
down_revision = 'c3490ae2d59c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'is_published')
    op.drop_column('posts', 'modified_at')
    op.drop_column('posts', 'created_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('modified_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('is_published', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
