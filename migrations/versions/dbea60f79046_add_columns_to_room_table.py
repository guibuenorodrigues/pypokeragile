"""add columns to room table

Revision ID: dbea60f79046
Revises: a0077792b639
Create Date: 2021-09-01 21:15:30.240754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbea60f79046'
down_revision = 'a0077792b639'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('rooms', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rooms', 'is_admin')
    op.drop_column('rooms', 'created_at')
    # ### end Alembic commands ###
