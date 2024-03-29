"""empty message

Revision ID: a1bbddb0d0bd
Revises: 
Create Date: 2019-10-24 23:30:04.330097

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a1bbddb0d0bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('table_name') as batch_op:
        batch_op.alter_column('text',
                              existing_type=sa.TEXT(),
                              nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('table_name') as batch_op:
        batch_op.alter_column('text',
                              existing_type=sa.TEXT(),
                              nullable=False)
    # ### end Alembic commands ###
