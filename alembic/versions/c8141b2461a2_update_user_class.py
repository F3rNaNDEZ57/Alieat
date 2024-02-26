"""update user class

Revision ID: c8141b2461a2
Revises: bcf06687083d
Create Date: 2024-02-27 00:02:23.995780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c8141b2461a2'
down_revision: Union[str, None] = 'bcf06687083d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.alter_column('user', 'add_line1',
#                existing_type=sa.VARCHAR(length=250),
#                type_=sa.String(length=256),
#                existing_nullable=False)
#     op.alter_column('user', 'add_line2',
#                existing_type=sa.VARCHAR(length=250),
#                type_=sa.String(length=256),
#                existing_nullable=False)
#     # ### end Alembic commands ###
#
#
# def downgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.alter_column('user', 'add_line2',
#                existing_type=sa.String(length=256),
#                type_=sa.VARCHAR(length=250),
#                existing_nullable=False)
#     op.alter_column('user', 'add_line1',
#                existing_type=sa.String(length=256),
#                type_=sa.VARCHAR(length=250),
#                existing_nullable=False)
#     # ### end Alembic commands ###


def upgrade() -> None:
    # Use batch operations for SQLite compatibility
    with op.batch_alter_table('user') as batch_op:
        batch_op.alter_column('add_line1',
                              existing_type=sa.VARCHAR(length=250),
                              type_=sa.String(length=256),
                              existing_nullable=False)
        batch_op.alter_column('add_line2',
                              existing_type=sa.VARCHAR(length=250),
                              type_=sa.String(length=256),
                              existing_nullable=False)


def downgrade() -> None:
    # Use batch operations for SQLite compatibility
    with op.batch_alter_table('user') as batch_op:
        batch_op.alter_column('add_line2',
                              existing_type=sa.String(length=256),
                              type_=sa.VARCHAR(length=250),
                              existing_nullable=False)
        batch_op.alter_column('add_line1',
                              existing_type=sa.String(length=256),
                              type_=sa.VARCHAR(length=250),
                              existing_nullable=False)
