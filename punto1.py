"""El valle de aburra afronta altas temperaturas año tras año, Cree una que permita 
calcular la temperatura media de la tierra partir de recibir 20 datos diarios de 
temperatura por 8 días diferentes.
"""

temperaturas = [
    {28, 34, 22, 37, 25, 36, 30, 23, 33, 26, 31, 38, 24, 27, 35, 32, 29},
    {24, 30, 36, 27, 34, 22, 33, 25, 37, 28, 31, 35, 26, 38, 23, 32, 29},
    {23, 30, 26, 36, 32, 27, 25, 38, 33, 22, 29, 31, 37, 28, 24, 35, 34},
    {35, 24, 33, 36, 31, 29, 28, 26, 32, 37, 25, 22, 34, 30, 23, 38, 27},
    {25, 27, 30, 36, 23, 33, 38, 31, 22, 35, 24, 28, 37, 26, 34, 32, 29},
    {34, 35, 27, 26, 36, 23, 38, 24, 37, 30, 28, 22, 29, 31, 32, 33, 25},
    {31, 22, 33, 38, 27, 26, 36, 34, 24, 29, 28, 30, 35, 32, 23, 25, 37},
    {27, 34, 35, 23, 22, 38, 32, 25, 36, 30, 28, 26, 37, 31, 33, 24, 29}
]


def temperatura_dia(temperaturas):
    medias = []
    for dia in temperaturas:
        media = sum(dia) / len(dia)
        medias.append(media)
    return medias

temperatura_media = temperatura_dia(temperaturas)

for i, media in enumerate(temperatura_media):
    print(f"Día {i+1}: {media} grados")
