"""n3

Revision ID: d546c9392a3f
Revises: 81d9c804ccbe
Create Date: 2025-03-28 09:49:16.756102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd546c9662a3f'
down_revision = '81d9c804ccbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.alter_column('category_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.alter_column('category_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###