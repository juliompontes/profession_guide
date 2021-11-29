#!/bin/bash
wget -r ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC*
mkdir rais_raw_data
7z x ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_CENTRO_OESTE.7z -o/home/user/projetos/rais/rais_raw_data
7z x ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_MG_ES_RJ.7z -o/home/user/projetos/rais/rais_raw_data
7z x ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_NORDESTE.7z -o/home/user/projetos/rais/rais_raw_data
7z x ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_NORTE.7z -o/home/user/projetos/rais/rais_raw_data
7z x ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_SP.7z -o/home/user/projetos/rais/rais_raw_data
7z x ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_SUL.7z -o/home/user/projetos/rais/rais_raw_data
rm -R ftp.mtps.gov.br
