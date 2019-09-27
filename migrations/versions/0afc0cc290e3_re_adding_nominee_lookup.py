"""re-adding nominee_lookup

Revision ID: 0afc0cc290e3
Revises: 68f4f2e6075c
Create Date: 2019-09-23 21:31:50.135128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0afc0cc290e3'
down_revision = '68f4f2e6075c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nominee_lookup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_nominee_lookup_name'), 'nominee_lookup', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_nominee_lookup_name'), table_name='nominee_lookup')
    op.drop_table('nominee_lookup')
    # ### end Alembic commands ###
