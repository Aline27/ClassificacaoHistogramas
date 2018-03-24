import sys
import numpy as np
import cv2
import glob
import cv
from matplotlib import pyplot as plt


def classification(image1, image2, method):

	color= ('b','g','r')
	soma=0
	for l,col in enumerate(color):
		hist1= cv2.calcHist ([image1], [l], None, [256] ,[0,256])
		hist2= cv2.calcHist ([image2], [l], None, [256] ,[0,256])	
		hist1 = cv2.normalize(hist1)
		hist2= cv2.normalize(hist2)
		result_comp=0
		if (method == 'correlation'):
			result_comp=cv2.compareHist(hist1, hist2, cv.CV_COMP_CORREL)
			soma=soma+result_comp
			print result_comp
		elif (method == 'chi-square'):
			result_comp=cv2.compareHist(hist1, hist2, cv.CV_COMP_CHISQR)
			soma=soma+result_comp
			print result_comp
		elif (method == 'intersection'):
			result_comp=cv2.compareHist(hist1, hist2, cv.CV_COMP_INTERSECT)
			soma=soma+result_comp
			print result_comp
		elif (method == 'bhattacharyya'):
			result_comp=cv2.compareHist(hist1, hist2, cv.CV_COMP_BHATTACHARYYA)
			soma=soma+result_comp
			print result_comp
	average=soma/3
	print ('A media e '+str(average))
	return average

	

#-----------------------------------------------------------
#Imagens de teste

vet_name=['hulk1','iron1','k3po1','magneto1','trooper1','vader1','volve1','hulk2','iron2','k3po2','magneto2','trooper2','vader2','volve2']
method=['correlation','chi-square','intersection','bhattacharyya']

#-----------------------------------------------------------
#Leitura das imagens na pasta

images= [cv2.imread(file) for file in glob.glob("Imagens/*png")]

#Armazenamento do nome das imagens

aux=glob.glob('Imagens/*.png')
name_images=aux

for cont in range(len(aux)):
	name_images[cont]=aux[cont].split('/')[1]
	name_images[cont]=name_images[cont].split('.')[0]

#------------------------------------------------------------
#Comparacao

cont_correl=0
cont_inter=0
cont_chi=0
cont_bhatta=0
for k in range (0,len(method)):
	for j in range (0,len(vet_name)):
		img_test= cv2.imread('Imagens/'+vet_name[j]+'.png',1)
		high_value=0
		lower_value=100000
		for i in range(0,len(images)):
			if vet_name[j] != name_images[i]:
				print ('--------------------------------------------------')
				print ('Metodo: '+method[k])
				print ('Combinacao: '+vet_name[j]+' e '+name_images[i])
				r_average=classification(img_test,images[i],method[k])
				if (r_average > high_value ):
					high_value=r_average
					high_name1=vet_name[j]
					high_name2=name_images[i]
				if (r_average < lower_value):
					lower_value=r_average
					lower_name1=vet_name[j]
					lower_name2=name_images[i]

		if (high_name1[0:3] == high_name2[0:3]):
			if (method[k] == 'correlation'):
				cont_correl=cont_correl+1.0
			elif (method[k] == 'intersection'):
				cont_inter=cont_inter+1.0
		if (lower_name1[0:3] == lower_name2[0:3]):
			if (method[k] == 'chi-square'):
				cont_chi=cont_chi+1.0
			elif (method[k] == 'bhattacharyya'):
				cont_bhatta=cont_bhatta+1.0

taxa_correl=(cont_correl/14.0)*100
taxa_bhatta=(cont_bhatta/14.0)*100
taxa_inter=(cont_inter/14.0)*100
taxa_chi=(cont_chi/14.0)*100

print('--------------------------------------------------')
print ('Correlacao: Acertos - '+ str(cont_correl)+' Taxa de acertos - '+ str(round(taxa_correl,2))+'%')
print ('Interseccao: Acertos -'+ str(cont_inter) + ' Taxa de acertos - '+str(round(taxa_inter,2))+'%')
print ('Chi-square: Acertos - '+ str(cont_chi)+ ' Taxa de acertos - '+str(round(taxa_chi,2))+'%')
print ('Bhattacharyya: Acertos -'+ str(cont_bhatta)+ ' Taxa de acertos - ' + str(round(taxa_bhatta,2))+'%')

