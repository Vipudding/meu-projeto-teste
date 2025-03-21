def validar_cep(cep, cidade):
    faixas_cep = {
        "Alumínio": range(18125000, 18130000),
        "Iperó": range(18560000, 18570000),
        "Araçariguama": range(18147000, 18150000),
        "Araçoiaba da Serra": range(18190000, 18195000),
        "Itu": range(13300000, 13315000),
        "Mairinque": range(18120000, 18125000),
        "Cabreúva": range(13315000, 13320000),
        "Capela do Alto": range(18195000, 18200000),
        "Salto": range(13320000, 13330000),
        "Salto de Pirapora": range(18160000, 18170000),
        "São Roque": range(18130000, 18147000),
        "Sarapuí": range(18225000, 18230000),
        "Sorocaba": range(18000000, 18110000),
        "Votorantim": range(18110000, 18120000),
        "Porto Feliz": range(18540000, 18550000),
    }

    if cidade not in faixas_cep:
        return False

    cep_int = int(cep)

    return cep_int in faixas_cep[cidade]