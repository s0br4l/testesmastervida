from django.db import models


class Antropometria(models.Model):
    nome = models.CharField('Nome usuário', max_length=250)
    n_user = models.IntegerField('N do usuario')
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    estatura = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    Ptronco = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Pcintura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Pabdomen = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Pquadril = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    PantebracoD = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    PbracoD = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    PcoxaD = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    PpernaD = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome


class Testes(models.Model):
    nome = models.CharField('Nome usuário', max_length=250)
    n_user = models.IntegerField('N do usuario')
    Dinamometro_1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Dinamometro_2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Sentar_levantar = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Ir_vir_1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Ir_vir_2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Marcha_1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Marcha_2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome


class Dexa(models.Model):
    nome = models.CharField('Nome usuário', max_length=250)
    n_user = models.IntegerField('N do usuario')
    BMC_gr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    FAT_MASS_gr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    LEAN_MASS_gr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    DXG_T = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMC_Arm_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMC_Arm_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMC_Trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMC_Leg_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMC_Leg_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMC_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    FAT_MASS_Arm_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    FAT_MASS_Arm_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    FAT_MASS_Trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    FAT_MASS_Leg_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    FAT_MASS_Leg_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    FAT_MASS_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    LEAN_MASS_Arm_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    LEAN_MASS_Arm_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    LEAN_MASS_Trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    LEAN_MASS_Leg_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    LEAN_MASS_Leg_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    LEAN_MASS_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    DXG_FAT_Arm_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    DXG_FAT_Arm_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    DXG_FAT_Trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    DXG_FAT_Leg_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    DXG_FAT_Leg_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    DXG_FAT_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_L_ARM_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_R_ARM_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_L_Ribs_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_R_Ribs_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_T_Spine_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_L_Spine_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_Pelves_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_L_Leg_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_R_Leg_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_head_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Area_Total_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_L_Arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_R_Arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_L_Ribs = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_R_Ribs = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_T_Spine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_L_Spine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_Pelves = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_L_Leg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_R_Leg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BMD_Total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    T_Score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Z_Score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome

