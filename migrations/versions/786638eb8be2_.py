"""empty message

Revision ID: 786638eb8be2
Revises: 
Create Date: 2023-03-30 22:22:54.347393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '786638eb8be2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('sex', sa.String(length=1), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('activityFactor', sa.Integer(), nullable=True),
    sa.Column('countdown', sa.Integer(), nullable=True),
    sa.Column('diet', sa.String(length=1), nullable=True),
    sa.Column('default_fat', sa.Integer(), nullable=True),
    sa.Column('default_carb', sa.Integer(), nullable=True),
    sa.Column('default_protein', sa.Integer(), nullable=True),
    sa.Column('default_kcal', sa.Integer(), nullable=True),
    sa.Column('fat', sa.Integer(), nullable=True),
    sa.Column('carb', sa.Integer(), nullable=True),
    sa.Column('protein', sa.Integer(), nullable=True),
    sa.Column('kcal', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('food',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cal', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('food_name', sa.String(length=10000), nullable=True),
    sa.Column('food_fat', sa.Integer(), nullable=True),
    sa.Column('food_carb', sa.Integer(), nullable=True),
    sa.Column('food_protein', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('macro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fat', sa.Integer(), nullable=True),
    sa.Column('carb', sa.Integer(), nullable=True),
    sa.Column('protein', sa.Integer(), nullable=True),
    sa.Column('kcal', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=10000), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=10000), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weight')
    op.drop_table('note')
    op.drop_table('macro')
    op.drop_table('food')
    op.drop_table('user')
    # ### end Alembic commands ###
