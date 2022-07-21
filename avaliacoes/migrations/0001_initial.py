# Generated by Django 4.0.6 on 2022-07-21 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antropometria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome usuário')),
                ('n_user', models.IntegerField(verbose_name='N do usuario')),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('estatura', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('Ptronco', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Pcintura', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Pabdomen', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Pquadril', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('PantebracoD', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('PbracoD', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('PcoxaD', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('PpernaD', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dexa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome usuário')),
                ('n_user', models.IntegerField(verbose_name='N do usuario')),
                ('BMC_gr', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('FAT_MASS_gr', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('LEAN_MASS_gr', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DXG_T', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMC_Arm_L', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMC_Arm_R', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMC_Trunk', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMC_Leg_L', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMC_Leg_R', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMC_Head', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('FAT_MASS_Arm_L', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('FAT_MASS_Arm_R', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('FAT_MASS_Trunk', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('FAT_MASS_Leg_L', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('FAT_MASS_Leg_R', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('FAT_MASS_Head', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('LEAN_MASS_Arm_L', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('LEAN_MASS_Arm_R', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('LEAN_MASS_Trunk', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('LEAN_MASS_Leg_L', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('LEAN_MASS_Leg_R', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('LEAN_MASS_Head', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DXG_FAT_Arm_L', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DXG_FAT_Arm_R', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DXG_FAT_Trunk', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DXG_FAT_Leg_L', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DXG_FAT_Leg_R', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('DXG_FAT_Head', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_L_ARM_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_R_ARM_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_L_Ribs_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_R_Ribs_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_T_Spine_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_L_Spine_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_Pelves_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_L_Leg_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_R_Leg_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_head_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Area_Total_cm3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_L_Arm', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_R_Arm', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_L_Ribs', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_R_Ribs', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_T_Spine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_L_Spine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_Pelves', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_L_Leg', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_R_Leg', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_Head', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMD_Total', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('T_Score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Z_Score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome usuário')),
                ('n_user', models.IntegerField(verbose_name='N do usuario')),
                ('Dinamometro_1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Dinamometro_2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Sentar_levantar', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Ir_vir_1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Ir_vir_2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Marcha_1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Marcha_2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]