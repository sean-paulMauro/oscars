"""adding rt + category_nominee

Revision ID: cfe744395a65
Revises: 0afc0cc290e3
Create Date: 2019-09-23 21:48:51.968012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfe744395a65'
down_revision = '0afc0cc290e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rotten_tomatoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.Column('consensus', sa.String(length=2000), nullable=True),
    sa.Column('score', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category_nominee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('odds', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('nominee_id', sa.Integer(), nullable=True),
    sa.Column('rt_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category_lookup.id'], ),
    sa.ForeignKeyConstraint(['nominee_id'], ['nominee_lookup.id'], ),
    sa.ForeignKeyConstraint(['rt_id'], ['rotten_tomatoes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category_nominee')
    op.drop_table('rotten_tomatoes')
    # ### end Alembic commands ###