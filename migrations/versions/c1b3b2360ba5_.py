"""empty message

Revision ID: c1b3b2360ba5
Revises: 
Create Date: 2018-07-20 14:00:09.083076

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c1b3b2360ba5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('home_beer_taste_beer_id_776e787e', table_name='home_beer_taste')
    op.drop_index('home_beer_taste_taste_id_7dff3de0', table_name='home_beer_taste')
    op.drop_table('home_beer_taste')
    op.drop_index('home_rating_beer_id_019c613b', table_name='home_rating')
    op.drop_table('home_rating')
    op.drop_index('auth_user_username_6821ab7c_like', table_name='auth_user')
    op.drop_table('auth_user')
    op.drop_index('auth_group_permissions_group_id_b120cbf9', table_name='auth_group_permissions')
    op.drop_index('auth_group_permissions_permission_id_84c5c92e', table_name='auth_group_permissions')
    op.drop_table('auth_group_permissions')
    op.drop_table('django_migrations')
    op.drop_table('home_brand')
    op.drop_index('django_admin_log_content_type_id_c4bce8eb', table_name='django_admin_log')
    op.drop_index('django_admin_log_user_id_c564eba6', table_name='django_admin_log')
    op.drop_table('django_admin_log')
    op.drop_table('django_content_type')
    op.drop_table('home_containertype')
    op.drop_index('auth_user_groups_group_id_97559544', table_name='auth_user_groups')
    op.drop_index('auth_user_groups_user_id_6a12ed8b', table_name='auth_user_groups')
    op.drop_table('auth_user_groups')
    op.drop_table('home_taste')
    op.drop_index('home_beer_bodyType_id_f0ecc2f1', table_name='home_beer')
    op.drop_index('home_beer_brand_id_f16fd460', table_name='home_beer')
    op.drop_index('home_beer_colour_id_655f6fb5', table_name='home_beer')
    op.drop_table('home_beer')
    op.drop_index('home_beer_containerType_beer_id_0647fd28', table_name='home_beer_containerType')
    op.drop_index('home_beer_containerType_containertype_id_45ef3f16', table_name='home_beer_containerType')
    op.drop_table('home_beer_containerType')
    op.drop_table('home_colour')
    op.drop_index('django_session_expire_date_a5c62663', table_name='django_session')
    op.drop_index('django_session_session_key_c0390e0f_like', table_name='django_session')
    op.drop_table('django_session')
    op.drop_index('auth_user_user_permissions_permission_id_1fbb5f2c', table_name='auth_user_user_permissions')
    op.drop_index('auth_user_user_permissions_user_id_a95ead1b', table_name='auth_user_user_permissions')
    op.drop_table('auth_user_user_permissions')
    op.drop_table('home_bodytype')
    op.drop_index('auth_group_name_a6ea08ec_like', table_name='auth_group')
    op.drop_table('auth_group')
    op.drop_index('auth_permission_content_type_id_2f476e4b', table_name='auth_permission')
    op.drop_table('auth_permission')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_permission',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('auth_permission_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='auth_permission_content_type_id_2f476e4b_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_permission_pkey'),
    sa.UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_permission_content_type_id_2f476e4b', 'auth_permission', ['content_type_id'], unique=False)
    op.create_table('auth_group',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('auth_group_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_group_pkey'),
    sa.UniqueConstraint('name', name='auth_group_name_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_group_name_a6ea08ec_like', 'auth_group', ['name'], unique=False)
    op.create_table('home_bodytype',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('home_bodytype_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('bodyTypeName', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='home_bodytype_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('auth_user_user_permissions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
    sa.UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq')
    )
    op.create_index('auth_user_user_permissions_user_id_a95ead1b', 'auth_user_user_permissions', ['user_id'], unique=False)
    op.create_index('auth_user_user_permissions_permission_id_1fbb5f2c', 'auth_user_user_permissions', ['permission_id'], unique=False)
    op.create_table('django_session',
    sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('session_key', name='django_session_pkey')
    )
    op.create_index('django_session_session_key_c0390e0f_like', 'django_session', ['session_key'], unique=False)
    op.create_index('django_session_expire_date_a5c62663', 'django_session', ['expire_date'], unique=False)
    op.create_table('home_colour',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('home_colour_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('colourNum', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('colourHex', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='home_colour_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('home_beer_containerType',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"home_beer_containerType_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('beer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('containertype_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['beer_id'], ['home_beer.id'], name='home_beer_containerType_beer_id_0647fd28_fk_home_beer_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['containertype_id'], ['home_containertype.id'], name='home_beer_containerT_containertype_id_45ef3f16_fk_home_cont', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='home_beer_containerType_pkey'),
    sa.UniqueConstraint('beer_id', 'containertype_id', name='home_beer_containertype_beer_id_containertype_id_b6071859_uniq')
    )
    op.create_index('home_beer_containerType_containertype_id_45ef3f16', 'home_beer_containerType', ['containertype_id'], unique=False)
    op.create_index('home_beer_containerType_beer_id_0647fd28', 'home_beer_containerType', ['beer_id'], unique=False)
    op.create_table('home_beer',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('home_beer_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('beerName', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('alcoholVolume', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('bodyType_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('brand_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('bottlePrice', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('canPrice', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('kegPrice', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('beerPhoto', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('colour_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['bodyType_id'], ['home_bodytype.id'], name='home_beer_bodyType_id_f0ecc2f1_fk_home_bodytype_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['home_brand.id'], name='home_beer_brand_id_f16fd460_fk_home_brand_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['colour_id'], ['home_colour.id'], name='home_beer_colour_id_655f6fb5_fk_home_colour_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='home_beer_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('home_beer_colour_id_655f6fb5', 'home_beer', ['colour_id'], unique=False)
    op.create_index('home_beer_brand_id_f16fd460', 'home_beer', ['brand_id'], unique=False)
    op.create_index('home_beer_bodyType_id_f0ecc2f1', 'home_beer', ['bodyType_id'], unique=False)
    op.create_table('home_taste',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('home_taste_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('tasteName', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='home_taste_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('auth_user_groups',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_user_groups_group_id_97559544_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_groups_pkey'),
    sa.UniqueConstraint('user_id', 'group_id', name='auth_user_groups_user_id_group_id_94350c0c_uniq')
    )
    op.create_index('auth_user_groups_user_id_6a12ed8b', 'auth_user_groups', ['user_id'], unique=False)
    op.create_index('auth_user_groups_group_id_97559544', 'auth_user_groups', ['group_id'], unique=False)
    op.create_table('home_containertype',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('containerTypeName', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='home_containertype_pkey')
    )
    op.create_table('django_content_type',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('django_content_type_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_content_type_pkey'),
    sa.UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_table('django_admin_log',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='django_admin_log_content_type_id_c4bce8eb_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='django_admin_log_user_id_c564eba6_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='django_admin_log_pkey')
    )
    op.create_index('django_admin_log_user_id_c564eba6', 'django_admin_log', ['user_id'], unique=False)
    op.create_index('django_admin_log_content_type_id_c4bce8eb', 'django_admin_log', ['content_type_id'], unique=False)
    op.create_table('home_brand',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('home_brand_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('brandName', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('countryOfOrigin', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='home_brand_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('django_migrations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_migrations_pkey')
    )
    op.create_table('auth_group_permissions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
    sa.UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq')
    )
    op.create_index('auth_group_permissions_permission_id_84c5c92e', 'auth_group_permissions', ['permission_id'], unique=False)
    op.create_index('auth_group_permissions_group_id_b120cbf9', 'auth_group_permissions', ['group_id'], unique=False)
    op.create_table('auth_user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('date_joined', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_user_pkey'),
    sa.UniqueConstraint('username', name='auth_user_username_key')
    )
    op.create_index('auth_user_username_6821ab7c_like', 'auth_user', ['username'], unique=False)
    op.create_table('home_rating',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('ratingValue', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('beer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('reviewText', sa.TEXT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['beer_id'], ['home_beer.id'], name='home_rating_beer_id_019c613b_fk_home_beer_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='home_rating_pkey')
    )
    op.create_index('home_rating_beer_id_019c613b', 'home_rating', ['beer_id'], unique=False)
    op.create_table('home_beer_taste',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('beer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('taste_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['beer_id'], ['home_beer.id'], name='home_beer_taste_beer_id_776e787e_fk_home_beer_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['taste_id'], ['home_taste.id'], name='home_beer_taste_taste_id_7dff3de0_fk_home_taste_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='home_beer_taste_pkey'),
    sa.UniqueConstraint('beer_id', 'taste_id', name='home_beer_taste_beer_id_taste_id_1ded2dcd_uniq')
    )
    op.create_index('home_beer_taste_taste_id_7dff3de0', 'home_beer_taste', ['taste_id'], unique=False)
    op.create_index('home_beer_taste_beer_id_776e787e', 'home_beer_taste', ['beer_id'], unique=False)
    # ### end Alembic commands ###
