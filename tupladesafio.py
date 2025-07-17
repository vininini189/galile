estoque = (
    ("mouse lg tech", 10),
    ("mic hyper x", 5),
    ("acer nitro 5", 3),
    ("webcam hd", 0)
)

print('produtos com menos de 5 unidades')
for i in estoque :
    if i[1] < 5:
        print(f'- {i[0]}')

    