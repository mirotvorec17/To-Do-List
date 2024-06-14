"""Добавить крайний срок к задачам

Revision ID: cd55319ff217
Revises: 
Create Date: 2024-05-21 22:44:21.552650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd55319ff217'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deadline', sa.Date(), nullable=False))
        batch_op.drop_column('date_created')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.DATETIME(), nullable=True))
        batch_op.drop_column('deadline')

    # ### end Alembic commands ###
