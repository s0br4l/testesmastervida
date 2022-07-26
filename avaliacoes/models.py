from django.db import models

class Testes_medidas(models.Model):
    nome = models.CharField('Nome usuário', max_length=250)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    estatura = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    Ptronco = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    Pcintura = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    Pabdomen = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    Pquadril = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    PantebracoD = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    PbracoD = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    PcoxaD = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    PpernaD = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    Dinamometro_1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Dinamometro_2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Sentar_levantar = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Ir_vir_1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Ir_vir_2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Marcha_1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Marcha_2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMC_gr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    FAT_MASS_gr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    LEAN_MASS_gr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    DXG_T = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMC_Arm_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMC_Arm_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMC_Trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMC_Leg_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMC_Leg_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMC_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    FAT_MASS_Arm_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    FAT_MASS_Arm_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    FAT_MASS_Trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    FAT_MASS_Leg_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    FAT_MASS_Leg_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    FAT_MASS_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    LEAN_MASS_Arm_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    LEAN_MASS_Arm_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    LEAN_MASS_Trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    LEAN_MASS_Leg_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    LEAN_MASS_Leg_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    LEAN_MASS_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    DXG_FAT_Arm_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    DXG_FAT_Arm_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    DXG_FAT_Trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    DXG_FAT_Leg_L = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    DXG_FAT_Leg_R = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    DXG_FAT_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_L_ARM_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_R_ARM_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_L_Ribs_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_R_Ribs_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_T_Spine_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_L_Spine_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_Pelves_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_L_Leg_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_R_Leg_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_head_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Area_Total_cm3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_L_Arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_R_Arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_L_Ribs = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_R_Ribs = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_T_Spine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_L_Spine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_Pelves = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_L_Leg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_R_Leg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_Head = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    BMD_Total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    T_Score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    Z_Score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)

    def __str__(self):
        return self.nome
