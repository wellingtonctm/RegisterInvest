"""empty message

Revision ID: e0d989eee172
Revises: 0d7ae1acce03
Create Date: 2022-12-22 20:44:09.554009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0d989eee172'
down_revision = '0d7ae1acce03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('negociacoes', schema=None) as batch_op:
        batch_op.drop_column('tipoMercado')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('negociacoes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tipoMercado', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
