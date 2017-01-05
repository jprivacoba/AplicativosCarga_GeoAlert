# -*- coding: utf-8 -*-
"""
@file:   test_cargaPrisma.py
@date:   Nov,  2016
@author: Arnol
"""

import logging
logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


import scripts.prismas.driverLoad_Prisma as dr
import scripts.prismas.uploadPrismas as uplpr
import time

t_ini = time.time()

# Variables
filen_chuqui = "C:\Users\Arnol\Gesecology\[Demo] Chuquicamata\datos\prismas\Prismas_2006.csv"
filen_mel = "C:\Users\Arnol\Desktop\copia Data MEL\Prismas\Norte_Inferior.txt"
filen_mel = "C:\Users\Arnol\Desktop\copia Data MEL\Prismas\Sur_Este.txt"

connStr = "PG: host='%s' port='%s' dbname='%s' user='%s' password='%s'" % ("152.231.85.227",
                                                                           "5432",
                                                                           "geoalert_template",
                                                                           "postgres",
                                                                           "Admin321")


myprismas = dr.loadPrisma_Mel(filen_mel)
uplpr.uploadPrisma(myprismas, connStr, "prismas", "prismas_consolidado")


t_fin = time.time()
logging.info("Elapsed time: %f", t_fin - t_ini)