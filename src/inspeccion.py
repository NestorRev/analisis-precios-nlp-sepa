def inspeccionar_provincia(df, codigo_iso):
    filtro = df[df['sucursales_provincia'] == codigo_iso]
    return filtro[['id_sucursal', 'sucursales_nombre', 'sucursales_localidad', 'sucursales_provincia', 'sucursales_latitud', 'sucursales_longitud']]
