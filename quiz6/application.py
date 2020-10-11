from flask import Flask,redirect,render_template,request
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import pandas as pd

txt = """
El Álamo

“Recuerden el Álamo” es un grito de batalla que se escucha muy a menudo en los Estados Unidos, pero la mayoría de la gente sabe muy poco o nada de los eventos que hicieron esta frase tan conocida y popular. Regresemos a los años 1800 para familiarizarnos con los eventos que condujeron a la formación de Texas y su entrada a los Estados Unidos.

La batalla del Álamo que tuvo lugar en 1836 es recordada por el valor de hombres norteamericanos como William B. Travis, Davy Crockett y James Bowie; sin embargo, también hubo muchos mexicanos luchando al lado de los norteamericanos que de alguna forma fueron olvidados en esta lucha por la independecia de Texas. Personajes como José Antonio Navarro y los tejanos, gente que había poblado la frontera mexicana de Texas y lucharon hombro a hombro con los norteamericanos, son olvidados por la mayoría de los narradores de esta historia.

José Antonio Navarro
Ubicada en San Antonio, Texas, la misión de San Antonio de Valero, conocida actualmente como El Álamo, había sido fundada para convertir la población indígena local a la cristiandad. Angel Navarro, padre de José Antonio llegó de España pero nació en Córcega. Por eso era conocido localmente como español, así que le fue muy fácil involucrarse en la alta sociedad del San Antonio de ese entonces. José Antonio Navarro fue uno de los pocos en San Antonio en recibir una instrucción académica. Cuando José Antonio, tuvo un accidente de niñez que lo dejó incapacitado físicamente, el joven volcó su atención a sus estudios. Su familia tenía una casa de piedra en un área del pueblo reservada para las personas de ascendencia europea. Se hacían llamar “los vecinos”. Los Navarro y otras familias de vecinos encabezaron la rebelión contra España, poniendo en riesgo todo lo que tenían.

La guerra contra España
23 años antes de la batalla del Álamo, Texas era parte de México que había sido colonizado años antes por España. Durante dos años, la comunidad tejana había tomado parte en una rebelión contra España. Su lucha por la independencia estaba arraigada en la economía. La corona de España sólo veía a Texas como una fuente de ingresos. El comercio de los mustangos que cabalgaban por los campos de Texas era una de las pocas formas en la que los tejanos podían ganarse la vida. Los caballos eran transportados al territorio norteamericano de Louisiana, donde se vendían o se cambiaban por provisiones.

Cuando el gobierno español declaró que todo el ganado silvestre era propiedad de la corona, muchos tejanos perdieron su única forma de ganarse la vida y por lo tanto se rebelaron. Pero el poderoso ejército español reprimió la rebelión tejana. Las personas fueron capturadas en San Antonio y encarceladas; los prisioneros fueron apiñados de tal modo que muchos murieron durante la primera noche. En los días siguientes el resto de los prisioneros fueron ejecutados delante de sus familias. José Antonio Navarro, cuya familia había ayudado a liderar la rebelión pudo escapar la matanza. Él y cientos de otros tejanos, buscaron refugio en los Estados Unidos.

Tres años después de que José Antonio huyera a los Estados Unidos, España declaró una amnestía general que le permitió regresar a Texas. Al regresar, se veía por todas partes evidencia del castigo de los españoles. La comunidad había sido devastada y muchos de los edificios estaban destruidos. La casa de los Navarro estaba en ruinas; José Antonio Navarro y los otros tejanos tuvieron que empezar a reconstruir sus vidas.

En 1821, después de una década de revolución, México obtuvo su independecia de España. José Antonio Navarro, culto, buen orador y bien relacionado, estaba listo para liderar a los tejanos y a Texas. En menos de un año, a los 26 años de edad fue nombrado alcalde de San Antonio.

Stephen F. Austin
El mismo año que México obtuvo su independencia, un joven que ayudaría a cambiar el curso de la historia de Texas llegó a San Antonio. Stephen F. Austin tenía el ambicioso plan de traer familias de Estados Unidos a Texas.  Los Austin de Missouri habían sido una de las familias más ricas del oeste. Pero en 1821 ya estaban arruinados. Stephen Austin vio a Texas como la tierra prometida, un lugar donde podría recuperar el buen nombre de su familia.

Austin distribuyó una carta en los Estados Unidos que fue circulada por la prensa, en la que describía a Texas como la tierra de la leche y la miel. Su mensaje llegó justo cuando Estados Unidos se estaba recuperando de una depresión económica. Cientos de colonos se enlistaron, aceptando convertirse al catolicismo y a ser ciudadanos mexicanos. Pudieron comprar tierras a precios razonables y en muchos casos las recibieron gratis.

Navarro se percató del potencial del plan de colonización de Austin y lo ayudó a alentar la inmigración estadounidense a Texas. También formaba parte de un grupo de líderes del norte de México que estaban de acuerdo con muchos de los conceptos del liberalismo económico clásico. Ellos querían que Texas se integrara a la economía del mercado internacional.

El plan de colonización de Austin fue un éxito. Tres años después de haber hecho un llamado a los colonos, 1800 personas vivían en su colonia de San Felipe. Navarro y Austin se habían convertido en dos de los hombres más influyentes en Texas.

El conflicto con México
Después de varios años de prosperidad, el gobierno de México decidió unir a Texas con el estado de Coahuila. Los tejanos protestaron contra esta decisión que según ellos acabaría con sus esperanzas de tener un estado independiente bajo el gobierno de México. En la década de 1820, la población de Texas era muy escasa y el gobierno mexicano tenía dificultades para atraer mexicanos al área. México llegó a un acuerdo con Stephen F. Austin, permitiendo que varios cientos de familias estadounidenses se mudaran a la región. Miles de pobladores adicionales pronto llegaron a Texas.

Cuando México abolió la esclavitud en todo el país, algunos inmigrantes de los Estados Unidos se negaron a cumplir la ley. Esto se sumó a las quejas acerca del tenso control político y económico sobre el territorio por el gobierno central en la Ciudad de México, que esperaba que sus ciudadanos fueran miembros de la Iglesia Católica, mientras que los pobladores estadounidenses eran protestantes. El gobierno mexicano preocupado por la gran cantidad de inmigrantes de los Estados Unidos en Texas, decretó una ley con el fin de cerrar la frontera. Ésta derrotó los planes que Austin y Navarro tenían para Texas. A pesar de esto, Austin sigió ayudando a los norteamericanos a venir a instalarse en Texas.

En 1833 Antonio López de Santa Ana llegó a ser presidente de México. En 1834, Santa Ana concentró el poder en la Ciudad de México. Disolvió el cuerpo legislativo estatal, limitó la autoridad de la milicia estatal y abolió la constitución federal. La respuesta fue inmediata. En Texas, los colonos de Estados Unidos empezaron a tener encuentros con los soldados mexicanos. Santa Ana se quedó en la Ciudad de México, pero envió seiscientas tropas a San Antonio. Él creía con cierta justificación, que la rebelión en Texas había sido instigada por fuerzas dentro de los Estados Unidos. El pánico cundió en la comunidad de colonos en Texas.

Al poco tiempo de que llegaran las tropas mexicanas enviadas por Antonio López de Santa Ana a San Antonio, éstas fueron atacadas por un ejército de rebeldes en Texas. Peleando con los norteamericanos había una compañía de voluntarios tejanos. No querían la independencia pero querían que se restituyera la constitución mexicana de 1824, que les daría más autonomía y respaldo para desarrollar sus intereses económicos y demás con mayor éxito en su propia área y región.

La pelea se extendió por varias semanas. Pero en diciembre de 1835, la mayor parte de las tropas mexicanas se habían refugiado en el Álamo. Con la llegada del invierno, ambos ejércitos estaban desmoralizados. Fue la deserción de un teniente mexicano que simpatizaba con la causa federalista, la que finalmente condujo a la derrota de las tropas mexicanas en 1835. El líder de las tropas mexicanas en el Álamo se entregó el 9 de diciembre. Las tropas regresaron a México en desgracia. La derrota fue humillante para el Presidente Antonio López de Santa Ana.

La Batalla del Álamo
Para fines de 1835, los tejanos habían logrado sacar a todos los soldados mexicanos de Texas. El tono y la dirección de la revolución cambiaron rápidamente de ser una guerra civil en México, a una lucha para separar Texas de México. En febrero de 1836, José Antonio Navarro y los líderes tejanos se reunieron para declarar la independencia. Mientras Navarro se dirijía a la asembea, un Santa Ana furioso se acercaba a San Antonio con más de cuatro mil hombres. El general mexicano sospechaba que los Estados Unidos respaldaba la reunión de los tejanos y amenazó con continuar su marcha hasta el mismo Washington D.C. Los tejanos que eran leales a México les dieron la bienvenida, pero entre muchos otros cundió el pánico. Muchos corrieron al campo para esconderse de la batalla inminente. Otros se encerraron en sus casas para tratar de proteger sus posesiones y su sustento. Y algunos se refugiaron en el Álamo, pensando que allí estarían a salvo.

Al llegar las tropas mexicanas a San Antonio, las fuerzas tejanas se atrincheraron en la misión de El Álamo utilizando algunas casas de sus cercanías como puestos de defensa avanzada. En la madrugada del 6 de marzo, unos 1.200 soldados mexicanos divididos en cuatro columnas atacaron la fortificación de forma simultánea por los cuatro lados. Penetraron en el interior de la guarnición matando a todos los defensores. Los civiles no combatientes (mujeres, niños y esclavos) que no murieron accidentalmente debido a los combates fueron respetados y se les permitió salir libremente. En las siguientes semanas, el ejército mexicano mataría a cientos de tejanos más. Esencialmente, los tejanos perdieron todas las batallas en el año de 1836. El ejército tejano fue destruido, derrotado y desbandado.

Después de la Batalla
Seis semanas después de la batalla del Álamo, unas vengativas fuerzas tejanas sorprendieron a Santa Ana cerca de un río llamado San Jacinto. Sam Houston al mando del ejérecito de Texas, exhortó a sus tropas con el grito de: “Recuerden el Alamo”. Los hombres que atacaron se jugaron el todo por el todo; estaban tan furiosos y era tanta su emoción, que después que la batalla terminó en 18 minutos y que el ejército mexicano fue derrotado y huía, sigieron matando. Esa victoria inmortalizó el grito de guerra de Texas: “Recuerden el Álamo”. Con la invocación de  “Recuerden el Álamo”, se envió un mensaje de compensación, de que el enemigo debe pagar por todo lo malo que hizo en la guerra.

Con la formación de la República de Texas ese mismo año, los tejanos y los anglos compartieron el poder en San Antonio durante varios años. Pero este incómodo arreglo llegó a su final, al llegar más y más gente nueva de los Estados Unidos. Todos los anglos que llegaron a San Antonio después de 1836 y que desconocían la contribución de los tejanos al movimiento de independencia, veían en cada mexicano un esteriotipo de Santa Ana. El sentimiento anti-mexicano impactó a Navarro personalmente cuando un colono anglo mató a Eugenio, su hermano más joven, pues sospechaba que era leal a México.

Mientras que otros tejanos eran perseguidos, Navarro, que ayudó a redactar la primera constitución del estado, aún era visto por los norteamericanos como un paladín de la revolución de Texas. Se convirtió en un desafiante vocero de los tejanos oriundos. En 1846, Texas fue admitido a los Estados Unidos como un estado esclavista. En 1853, Navarro escribió sus “puntos históricos” acerca de la participación de los tejanos en la formación de Texas. Su relato les hizo recordar tanto a los tejanos oriundos como a los norteamericanos, que la lucha por Texas comenzó mucho antes que se pronunciaran las palabras “Recuerden el Alamo”. Navarro murió en 1871.
"""

# stopwords = pd.read_csv('./material/SpanishStopWords.csv', encoding = "ISO-8859-1")
# stopwords = [s[0] for s in stopwords.values.tolist()]
# q6 = [s for s in stopwords if s in txt]
# print(q6)
# word_tokens = word_tokenize(txt)
# txt_list = [w for w in word_tokens] 
txt_list = txt.split(' ')
# q7 = [(txt_list[i-1], txt_list[i+1]) for i, w in enumerate(txt_list) if w in stopwords]
# print(q7)




# # EB looks for an 'application' callable by default.
application = Flask(__name__)

# # stop_words = set(stopwords.words('english')) 
# example_sent = "This is a sample sentence, showing off the stop words filtration."
  
# stop_words = set(stopwords.words('english')) 
  
# word_tokens = word_tokenize(example_sent) 
  
# filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
# filtered_sentence = [] 
  
# for w in word_tokens: 
#     if w not in stop_words: 
#         filtered_sentence.append(w) 
  
# print(word_tokens) 
# print(filtered_sentence) 


@application.route('/')
def index():
   return render_template('index.html')

@application.route('/search_largest_n', methods=['GET'])
def search_largest_n(number=5):
    freq = request.args.get('freq')
    word = request.args.get('word')
    ansd = []
    ansc = []
    if freq:
      counter = Counter(txt_list)
      for k, v in counter.items():
          freq = int(freq)
          if freq>0:
            ansc.append([k, v])
          freq -= 1
      print("dda", ansc)
    if word:
      sentence_list = txt.split('.')
      
      for sentence in sentence_list:
          if word in sentence:
              ansd.append(sentence_list)
      print('aad', ansd)
      
    return render_template('large_n.html', ci=ansc, di=ansd)
  

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()