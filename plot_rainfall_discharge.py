import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU


def plot_chuva_vazao(df_chuva, df_vazao, path, vazao=False, df_nivel=None, figsize = [70,30], labels = ['Nível', 'Precipitação'], units = ['cm', 'mm'], locator = ['weekday',4]):
	
	'''
	df_chuva : pd.DataFrame com colunas = 'Data', 'Chuva'
	df_vazao : pd.DataFrame com colunas = 'Data', 'Vazao'
	nivel : True para plotar nivel ao invés de vazao
	df_nivel : pd.DataFrame com colunas = 'Data', 'Nivel'
	labels : [ylabel da esquerda, ylabel da direita]
	'''
	
	
	# instancing the axes
	
	fig, ax1, ax2= None, None, None
	fig, ax1 = plt.subplots()
	
	ax2 = ax1.twinx()
	
	#tamanho da figura
	fig.set_size_inches(figsize[0],figsize[1])
	[ax1.spines[side].set_linewidth(3) for side in ax1.spines] #largura do enquadramento
	
	df_chuva.plot(ax=ax2, x = 'Data', y = 'Thiessen', kind='area',legend=False, color = 'Black')
	# plt.plot(df_chuva['Data'],df_chuva['Thiessen'])
	df_vazao.plot(ax=ax1, x = 'Data', y = 'Nivel', kind = 'line', legend=False,linewidth=7.0)
	
	
	
	'''
	Modificações
	'''
		
	#limits
	minimo=df_vazao['Data'].min()
	maximo=df_vazao['Data'].max()
	ax2.set_xlim(minimo, maximo)
	ax2.set_ylim(-1200,0)
	ax1.set_ylim(0,1200)
	
	#labels
	ax2.set_ylabel(labels[1], fontsize=70)
	ax1.set_ylabel(labels[0], fontsize=70)
	ax1.set_xlabel('')
	ax2.set_xlabel('')
	
	#ticks
	ax2.tick_params(labeltop=True, top=True, labelsize=60)
	ax1.tick_params(labeltop=True, labelbottom=True, bottom=True, top=True, labelsize=60)
	ax1.yaxis.set_major_formatter(mticker.FormatStrFormatter(r'%d {}'.format(units[0])))
	ax1.tick_params(which='major',width=7, length=20)
	ax2.tick_params(which='major',width=7, length=20)
	ax1.tick_params(which='minor',width=7, length=20, labelsize=60)

	lbls = [str(int(item*-1))+' '+ units[1] for item in ax2.get_yticks().tolist()] #adding unit and removing the minus sign
	ax2.set_yticklabels(lbls)

	if locator[0]=='weekday':
		pass
		# ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=locator[1]))
		# # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
		# ax1.xaxis.set_minor_locator(mdates.WeekdayLocator(interval=locator[1]))
		# ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
	
	elif locator[0]=='month':
		pass
		# ticks_to_use = df_vazao.index[::20]
		# labels = [ i for i in ticks_to_use ]
		# ax1.set_xticks(ticks_to_use)
		# ax1.set_xticklabels(labels)
		# ax1.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=locator[1]))
		# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
		# ax1.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=locator[1]))
		# ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
	
	print(ax1.get_xticks().tolist())
	#grid
	ax1.grid(which='both')
	ax2.grid(which='both')
	
	print(path)
	plt.savefig(path)
