# ClassificacaoHistogramas

-Autora: Aline de Oliveira

-Descrição: Utilizando histogramas, constru um classificador que receba uma imagem de teste e compare com as 13 restantes. 
Repita esse processo até que todas as 14 imagens tenham sido utilizadas como imagem de teste. 
Calcule a taxa de acerto para os 4 métodos métodos de comparação implementados no OpenCV: 
    CV_COMP_CORREL Correlation
    CV_COMP_CHISQR Chi-Square
    CV_COMP_INTERSECT Intersection
    CV_COMP_BHATTACHARYYA Bhattacharyya distance 

- Exemplo de entrada 
	$python exercicio2.py

-Resultado: Na saída será exibido a quantidade e a taxa de acertos de cada método. Além disso, anteriormente será apresentado 
todas as comparações realizadas e os resultadas dos métodos. Para cada comparação, tem-se 3 valores resultantes, uma vez que foi 
calculado o histograma de cada canal da imagem rgb. O resultado final é calculado com base na média desses três valores. 
A verificação da similaridade foi feita considerando-se que nos métodos Chi-Square e Bhattacharrya o menor valor final 
representa a maior similaridade, já nos métodos Correlation e Intersection o maior valor final representa a maior similaridade.
