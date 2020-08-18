class tienda (object):
    compra_total=float(input("digite el total de la compras :"))
    descuento= compra_total*0.15
    total_pag=compra_total-descuento
    pass
tiendasD1=tienda()
print(f"el valor total a apgr es :{tiendasD1.total_pag}")


