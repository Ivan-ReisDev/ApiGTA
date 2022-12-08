from flask import Flask, jsonify, request

app = Flask(__name__)

personagens = [
    {'id': 1,
     'nome': 'Michael De Santa',
     'negocios': 'Produtor de Filmes',
     'descricao': 'Michael é um ex-assaltante de banco e criminoso conhecido, que fingiu sua morte para se aposentar e viver uma vida pacífica com sua família em Los Santos. No entanto, ele sofre com seu relacionamento doentio com eles e logo é puxado de volta para sua vida criminosa, forçando-o a voltar aos velhos tempos. A história de Michael gira em torno de como seu estilo de vida aparentemente idílico e tranquilo é interrompido quando seus demônios do passado e erros moralmente comprometedores voltam para assombrá-lo.',
     'nacionalidade': 'Americano',
     'nascido': '1965/1968',
     'foto': 'https://static.wikia.nocookie.net/gta/images/a/a0/MichaelDeSanta-GTAV.png/revision/latest?cb=20200912165755&path-prefix=pt'},

    {'id': 2,
     'nome': 'Trevor Philips',
     'negocios': 'Trevor Philips Enterprises',
     'descricao': 'Trevor é um criminoso conhecido e ex-ladrão de banco com um passado complicado, que mais tarde fundou sua própria empresa, Trevor Philips Enterprises, operando com tráfico de drogas e contrabando de armas no Blaine County. Ele é amigo de Ron Jakowski e Wade Hebert, que trabalham para sua empresa, bem como do melhor e mais antigo amigo de Michael, que ele acreditava estar morto por quase uma década depois que ele fingiu sua morte para se aposentar da vida criminosa. Trevor é conhecido por ter um comportamento geralmente imprudente e muito agressivo, mas ele também é muito leal e respeita profundamente todos aqueles próximos a ele. A história de Trevor se concentra em como suas ações têm consequências para ele e seus amigos, e para ele chegar a um acordo com as ações anteriores de Michael. Trevor mais tarde também torna-se amigo do terceiro protagonista, Franklin, tornando-se uma espécie de mentor para ele.',
     'nacionalidade': 'Canadense'},

    {'id': 3,
     'nome': 'Franklin Clinton',
     'negocios': 'Assaltos',
     'descricao': 'Franklin nasceu e foi criado no Sul de Los Santos, quando criança, ele era amigo de Tanisha Jackson, Lamar Davis e Tonya Wiggins, todos estavam destinados a serem Gangsters como o pessoal de suas famílias de rua, mas Franklin e Tanisha queriam mais que isso.',
     'nacionalidade': 'Americano',
     'nascido': '1988',
     'foto': 'https://static.wikia.nocookie.net/gta/images/f/fa/FranklinClinton-GTAO-2021.png/revision/latest/scale-to-width-down/350?cb=20211214131245&path-prefix=pt'
     },

    {'id': 4,
     'nome': 'James de Santa',
     'negocios': 'Desconhecido',
     'descricao': 'Jimmy nasceu em 1993, ele cresceu e gostava muito de seus pais, irmã e até de seu "tio" Trevor Phillips. Porém em 2004, Michael teve que sair da vida de crimes e à única forma de fazer isso era forjando sua própria morte. Então Michael e sua família se mudarão para Los Santos.',
     'nacionalidade': 'Americano',
     'nascido': '1993',
     'foto': 'https://static.wikia.nocookie.net/gta/images/d/df/JimmyjamesGTAV.png/revision/latest/scale-to-width-down/350?cb=20170803035737&path-prefix=pt'
     },

    {'id': 5,
     'nome': 'Lester Crest',
     'negocios': 'Hacker',
     'descricao': 'De modo geral, o papel de Lester em Grand Theft Auto V e Online é ajudar os protagonistas nos planejamentos de golpes e também como um hacker, capaz de derrubar sistemas de segurança de diversos locais altamente protegidos. Ele também tem um veículo próprio, um Declasse Asea azul, mas ele só o utiliza em Grand Theft Auto Online, o jogador não pode usar no modo história, mas pode comprá-lo no GTA Online.',
     'nacionalidade': 'Americano',
     'nascido': 'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/3/36/Lester_photo_nextgen.png/revision/latest/scale-to-width-down/350?cb=20150623030751&path-prefix=pt'
     },

      {'id': 6,
     'nome': 'Abigail Mathers',
     'negocios': 'Desconhecido',
     'descricao': 'Não se sabe muito sobre a historia de Abigail antes do jogo, sabe-se que ela era assistente do produtor de TV/Cantor Frank Mathers e que ele abandonou sua esposa e 5 filhos para ficar com ela.',
     'nacionalidade': 'Americano',
     'nascido': 'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/2/2d/AbigailMathers-GTA5.png/revision/latest/scale-to-width-down/350?cb=20161215125926&path-prefix=pt'
     },

      {'id': 7,
     'nome': 'Agente 14',
     'negocios': 'IAA',
     'descricao': 'Pouco se sabe sobre o Agente 14, como ele fala muito pouco sobre a sua organização. Após ele se apresentar para os protagonistas online, logo ele diz que não estão ajudando ele e que ele não está envolvido, apenas é "um cara fazendo um favor".',
     'nacionalidade': 'Desconhecido',
     'nascido': 'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/3/3e/Agent_14.jpg/revision/latest?cb=20170626151201&path-prefix=pt'
     },

      {'id': 8,
     'nome': 'Agente ULP ou Bernard',
     'negocios': 'IAA',
     'descricao': 'Em algum momento anterior a 2008, ele tornou-se um agente secreto do governo e começou a trabalhar para o United Liberty Paper, posteriormente revelado ser uma fachada para a International Affairs Agency (IAA). Ele nasceu em algum momento entre 1943 e 1963 e menciona uma carreira militar passada no Exército dos EUA. Ele tem uma histórico de trabalho com traficantes de drogas na costa oeste da América e tem laços históricos com russos desde o final dos anos 80 e início dos anos 90, quando começaram a emigrar para a América com passaportes israelenses. Por sua própria admissão, ele foi "o primeiro a entrar (para a Rússia) em 91 e o primeiro a sair em 11". Ele também tem um histórico de operações durante as guerras iugoslavas enquanto fala sérvio (para Niko).',
     'nacionalidade': 'Desconhecida',
     'nascido': '1943/1963',
     'foto': 'https://static.wikia.nocookie.net/gta/images/2/27/TheContact-GTAV.png/revision/latest?cb=20191022174604&path-prefix=pt'
     },

      {'id': 9,
     'nome': 'Ahron Ward',
     'negocios': 'Traficante de drogas e Servidor do Burger Shot ',
     'descricao': 'Ahron Ward só é visto durante uma missão em que Michael De Santa leva seu filho Jimmy De Santa para pegar algumas drogas. Ele entrega uma bolsa de plástico contendo um pó branco para Jimmy e Jimmy solicitando o "especial" também uma bebida com um anestésico comumente usado por veterinários, que mais tarde é usado para drogar Michael. Ahron trabalha no Burger Shot em Vespucci.',
     'nacionalidade': 'Americana',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/e/eb/Burgerdrug.jpg/revision/latest/scale-to-width-down/350?cb=20180110205542&path-prefix=pt'
     },

      {'id': 10,
     'nome': 'Al Di Napoli',
     'negocios': 'Ator de cinema',
     'descricao': 'Al Di Napoli é um ator de cinema e teatro, italo-americano viciado em drogas e álcool. No site do jogo classicvinewood.com, há um filme de ação estrelado por Al Di Napoli chamado The Redeemer, criado em 1989 e produzido pela Dreyfuss Productions. O guia Vinewood Star Tours afirma que Di Napoli sofreu uma overdose no The Gentry Manor Hotel em 2002 "depois que um chimpanzé explodiu uma bola 8 em seu traseiro com uma pistola de água". Em 2008, ao não realizar shows e nem atuar em filmes ou TV em Los Santos ou Liberty City, Al vive em Vice City. Al afirma não gostar da atmosfera de Los Santos e não entende por que tantos atores adoram lá. Ele também irrita Luis Lopez perguntando quando ele e Tony estão expandindo os clubes para Vice City. Ele é um usuário do Bleeter em 2013, e sempre escreve que está sóbrio "novamente". Ele é uma das famosas celebridades na Calçada da Fama em Vinewood, com sua estrela ao oeste do Oriental Theater.',
     'nacionalidade': 'Ítalo-americano',
     'nascido': 'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/d/d5/AlDiNapoli-TBOGT.png/revision/latest?cb=20171024182802&path-prefix=pt'
     },

      {'id': 11,
     'nome': 'Albert Stalley',
     'negocios': 'Policial',
     'descricao': 'Stalley pode ser visto durante O Golpe à Joalheria dando problemas a Franklin. Ele é mais tarde ameaçado por Michael enquanto ele e sua equipe estão deixando a joalheria Vangelico. Seu nome é revelado quando ele está sendo entrevistado no Weazel News sobre o assalto. Durante a entrevista ele mencionou a citação que Michael disse para ele, chamando a atenção de Trevor, que está ouvindo ele enquanto faz sexo com Ashley Butler.',
     'nacionalidade': 'Desconhecido',
     'nascido': 'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/7/71/AlbertStalley-GTAV-next2.jpg/revision/latest?cb=20180922024205&path-prefix=pt'
     },

      {'id': 12,
     'nome': 'Amanda De Santa',
     'negocios': 'Stripper e Prostituta (Antigamente)',
     'descricao': 'Amanda De Santa é uma ex-stripper, que se casou com Michael Townley com quem teve dois filhos, James e Tracey Townley. Após viverem felizes por um tempo, a única coisa que Amanda se preocupava era com seu marido, que ainda se envolvia no mundo do crime com Trevor Philips e Bradley Snyder. Até que um dia Michael encontra uma saída, com a ajuda de um agente corrupto do FBI, Dave Norton, Michael simularia sua morte e se mudaria a Los Santos, com um novo sobrenome, De Santa. Após ser convencida por Michael, Amanda aceita o plano e o ajuda durante um falso assalto ao Banco Central de Ludendorff, sua cidade natal. Após o plano dar certo, Amanda e sua família se mudam a Los Santos e lá recomeçam suas vidas em um bairro luxuoso, Rockford Hills, com uma mansão enorme e oito dígitos ($ 25.000.000,00) todo mês na conta de Michael. Porém, toda essa felicidade durou pouco, por conta do mal uso o dinheiro da conta de Michael começou a se acabar, além de Amanda e seu marido viverem se traindo, e assim, os acontecimentos de Grand Theft Auto V começam.',
     'nacionalidade': 'Americano',
     'nascido':'1970',
     'foto': 'https://static.wikia.nocookie.net/gta/images/2/2c/Amanda-GTAV.png/revision/latest/scale-to-width-down/350?cb=20161222131653&path-prefix=pt'
     },

      {'id': 13,
     'nome': 'Andee ',
     'negocios': 'DJ',
     'descricao': 'Andee é a DJ da rádio Lips 106 que aparece no Grand Theft Auto III e Grand Theft Auto: Liberty City Stories. Em 1998 ela compartilha a locução com Cliff Lane, porém em 2001 ele é despedido por ser muito vulgar com os adolescentes. Em 1998, Andee diz que gostaria de ser a única DJ da rádio. Justamente em 2001 seu desejo torna-se realidade.',
     'nacionalidade': 'Desconhecido',
     'nascido':'Desconhecido',
     'foto': 'Desconhecido'
     },

      {'id': 14,
     'nome': 'Andreas Sanchez',
     'negocios': 'Agente do FIB',
     'descricao': 'Sua aparição mais importante é na missão "O Encerramento", onde Michael De Santa vai se encontrar com Dave Norton, que prometeu se livrar dele e do problema no assalto a nove anos atrás, mas quando ele pergunta por isso, Dave diz que tem um problema, depois disso Steve Haines e o Agente Sanchez chegam, e uma discussão começa pelo fato de Haines querer prender Michael pelas "transgressões de cada porra de crime que existe no mundo". Alguns segundos depois chega a IAA e o FIB para prender todos que estavam ali, e a Merryweather chega com um Buzzard de ataque, mandando todos abaixarem as armas. O Agente Sanchez se revela um traidor, revelando que foi ele que chamou a equipe do F.I.B, no meio desse impasse, um agente do F.I.B dá um tiro na perna de Haines, pelo fato dele não ter abaixado sua arma, e de raiva, Steve dá um tiro fatal na cabeça do Agente Sanchez, começando dai um conflito entre a IAA, F.I.B, Dave Norton e Trevor (Trevor Philips aparece no meio da missão, matando o piloto do Buzzard). Depois dessa missão ele não é mais mencionado.',
     'nacionalidade': 'Mexicano-Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/9/9d/AndreasSanchez-GTAV.png/revision/latest/scale-to-width-down/350?cb=20160920161333&path-prefix=pt'
     },

      {'id': 15,
     'nome': 'Anita Mendoza',
     'negocios': 'atriz, cantora pop e coreógrafa',
     'descricao': 'Anita é uma atriz, cantora pop e coreógrafa da década de 1990 que se tornou jurada no programa de TV Fame or Shame. Durante o show, ela aprova os insultos de Hugh Harrison a Lazlow Jones e simplesmente considera isso como sendo parte do "humor britânico". Anita menciona que Lazlow dormiu com uma mulher acima do peso em troca de colocá-la até as finais. Lazlow inicialmente nega isso antes de confirmá-lo.',
     'nacionalidade': 'Americana',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/5/51/Fame_or_Shame_GTAV_Judge_Anita_Mendoza.jpg/revision/latest/scale-to-width-down/350?cb=20161222132128&path-prefix=pt'
     },

      {'id': 16,
     'nome': 'Antonia Bottino',
     'negocios': 'Cartel de drogas',
     'descricao': 'Antônia é a filha do Ex-chefe da Gangue Família Gambetti, Sammy Bottino. Segundo ela, em 2007, uma acusação de assassinato  fez ela e sua família  esconder-se no Oeste. Ela diz que eles "... escondíamos em cidades Caipiras cheia de buracos onde ninguém iria nos procurar."',
     'nacionalidade': 'Liberty City',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/e/e1/Antonia_BottinoGTAV.jpg/revision/latest/scale-to-width-down/350?cb=20161222132951&path-prefix=pt'
     },

      {'id': 17,
     'nome': 'Ashley Butler',
     'negocios': 'The Lost',
     'descricao': 'Ashley nasceu em Liberty City e conhecia vários dos membros da The Lost desde a infância, incluindo Johnny K. Depois de ingressar na The Lost ela se tornou a namorada de Johnny e também se tornou uma viciado em drogas, o uso de cocaína e metanfetamina. Seus vícios, juntamente com a sua infidelidade (Que era muitas vezes induzidas por seu desejo de obter medicamentos baratos), levou a Johnny romper com ela, que teve um efeito devastador na vida de Ashley, severamente aumentando seu problema com as drogas.',
     'nacionalidade': 'Americana',
     'nascido':'1981',
     'foto': 'https://static.wikia.nocookie.net/gta/images/d/d9/Ashley_Butler_Beta.png/revision/latest?cb=20170119143335&path-prefix=pt'
     },

      {'id': 18,
     'nome': 'Barbara Watkins',
     'negocios': 'Desempregada',
     'descricao': 'Ela foi a um encontro com Simeon Yetarian mas foi presumivelmente obrigada a pagar o encontro, porque ele "esqueceu" sua carteira. Ela posta mensagens no Lifeinvader do Simeon, dizendo-lhe para parar de mandar mensagens, e que ela nunca mais quer vê-lo novamente. Seu perfil no Lifeinvader é privado.',
     'nacionalidade': 'Desconhecido',
     'nascido':'Desconhecido',
     'foto': 'Desconhecido'
     },

      {'id': 19,
     'nome': 'Barry',
     'negocios': 'Ativista',
     'descricao': 'Ele é um ativista que visa a legalização da maconha. Barry tem um encontro com cada protagonista (Michael De Santa, Trevor Philips e Franklin Clinton) e os vende a sua maconha especial, o que lhes provoca alucinações.',
     'nacionalidade': 'Desconhecido',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/0/05/Barry_cara.png/revision/latest?cb=20170314162007&path-prefix=pt'
     },

      {'id': 20,
     'nome': 'Beverly Felton',
     'negocios': 'Paparazzi',
     'descricao': 'Não se sabe muito sobre a vida de Beverlly antes dos acontecimento do jogo. apenas que ele tem uma relação de amor e ódio com as celebridades. Ele é obcecado por detalhes muito pequenos sobre suas vidas e quer que todos saibam, vendendo suas fotos altamente exclusivas por muito caro à jornais e revistas da cidade.',
     'nacionalidade': 'Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/1/17/Beverly-GTAV.png/revision/latest?cb=20151103161925&path-prefix=pt'
     },

      {'id': 21,
     'nome': 'Bradley Snider',
     'negocios': 'Assaltante',
     'descricao': 'Não se sabe muito sobre Bradley, apenas que ele nasceu em North Yankton e lá começou uma vida criminosa até conhecer Michael Townley e Trevor Philips, ele acabou virando amigo de ambos e juntos começaram a praticar crimes grandes atê que Michael diminuiu a frequência de assaltos com os dois, o que desencadeou uma raiva de Michael em Brad.',
     'nacionalidade': 'Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/e/e9/Brad-GTAV-prologue.png/revision/latest/scale-to-width-down/350?cb=20161212132013&path-prefix=pt'
     },

    {'id': 22,
     'nome': 'Tracey De Santa',
     'negocios': 'Desempregada',
     'descricao': 'Tracey nasceu em North Yankton por volta de 1991, sendo dois anos mais velha que Jimmy, seu irmão. Lá ela era feliz com sua família mas não se tinha muitas oportunidades em North Yankton, sem contar que seu pai era um ladrão profissional. Após os acontecimentos do O Prólogo, eles se mudam para Los Santos capital de San Andreas. Desde que chegaram lá, a família dos De Santa, tinham ambições, Tracey sonhava em ser famosa, não importava como, Amanda e Michael viviam traindo um ao outro, Michael com prostitutas e Amanda com outros homens, já Jimmy, o irmão mais novo de 20 anos que ainda mora as custas dos pais.',
     'nacionalidade': 'Americana',
     'nascido':'1991',
     'foto': 'https://static.wikia.nocookie.net/gta/images/4/4f/Tracey_De_Santa.png/revision/latest?cb=20131213015731&path-prefix=pt'
     },

     {'id': 23,
     'nome': 'Solomon Richards',
     'negocios': 'Proprietário da Richards Majestic Productions e Diretor de Cinema',
     'descricao': 'Solomon Richards é um produtor de cinema bem sucedido e proprietário da Richards Majestic Productions desde 1978 uma empresa de cinema que ele herdou de seu pai um clássico produtor de Vinewood chamado David Richards. Ele começou sua carreira produzindo filmes de seu pai, mas depois começou a produzir sozinho e eventualmente ganhou fama na época de 1970. com Filmes aclamados pela crítica nos meados de 1980. Ele teve um relacionamento um pouco complicado com uma das atrizes mais famosas da época Leonora Johnson, ela o considerava um "fake" de seu pai e se recusou a concluir um filme que ele estava a produzir naquele momento. Devido a "diferenças artísticas" e uma grande antipatia por Leonora, eventualmente fez Solomon ser um dos suspeitos pelo assassinato dela, na época. (Mas tarde sabemos que o assassino foi Peter Dreyfuss. mas ele nunca foi acusado devido a falta de provas). No momento em que o jogo acontece, a Richards Majestic Productions está com dificuldades financeiras, após o fracasso econômico de uma de suas produções mais recentes. Cansado da industria de cinema, Solomon tenta recuperar o prestigio de seu estúdio e se aposentar depois de fazer um ultimo filme chamado: Meltdown ',
     'nacionalidade': 'Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/1/18/SolomonRichards2-GTAV.png/revision/latest?cb=20160823142413&path-prefix=pt'
     },

     {'id': 24,
     'nome': 'Lamar Davis',
     'negocios': 'Tráfico de drogas, Roubo de carros e Fraude de cartão de crédito.',
     'descricao': 'Lamar cresceu junto a Franklin, Tanisha Jackson e Tonya Wiggins, eles tiveram uma infância difícil e complicada, já no meio de Gangues desde cedo. Lamar sempre teve uma personalidade positiva, sarcástica e nunca era muito inteligente, fazendo alguns de seus planos darem errado, quando de maior, ele começou a se envolver em crimes junto a Franklin.',
     'nacionalidade': 'Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/6/61/LamarDavis-GTAOe-2021Portrait.png/revision/latest/scale-to-width-down/350?cb=20220107141950&path-prefix=pt'
     },

     {'id': 25,
     'nome': 'Wade Hebert',
     'negocios': 'Vagabundo',
     'descricao': 'Wade é visto pela primeira vez ao lado de Ron Jakowski tentando acalmar Johnny Klebitz depois que Trevor teve relações sexuais com a namorada de Johnny, Ashley Butler , que terminou com Trevor matando Johnny e iniciando uma guerra entre ele e o The Lost MC; Wade se junta a Trevor em seus ataques contra a gangue. Mais tarde, Trevor pede a Wade que procure Michael Townley , que Wade localiza em Los Santos , após várias tentativas e ameaças fracassadas de Trevor, sob o nome "Michael De Santa". Eles se mudam para o apartamento do primo de Wade, Floyd , para desgosto de Floyd. Wade também ajuda Trevor a explorar um porto em busca de um assalto. Após um incidente no apartamento de Floyd, que resulta na morte de Floyd e de sua namorada,  Debra , Trevor, na tentativa de impedir Wade de descobrir sua morte, afirma que Floyd e Debra "desapareceram", assim como os velhos amigos de Wade, antes de assumir o clube de strip Vanilla Unicorn e pedir dois strippers para assistir a Wade. Wade permanece com eles, mesmo após o enredo principal, e até mantém um diálogo com ele, alegando que cada vez que ele tenta sair, os strippers fazem outra dança.',
     'nacionalidade': 'Americano',
     'nascido':'Desconhecido',
     'foto':'https://static.wikia.nocookie.net/gta/images/f/fc/Wade.png/revision/latest/scale-to-width-down/350?cb=20151022154805&path-prefix=pt'
     },

     {'id': 26,
     'nome': 'Devin Weston',
     'negocios': 'Merryweather Security',
     'descricao': 'Weston é um bilionário que fez fortuna comprando e vendendo ações, principalmente da Merryweather Security, que foi onde mais lhe deu lucro. Aos poucos ele criou sua própria companhia e começou a investir em outras organizações e atê mesmo em pessoas.',
     'nacionalidade': 'Americano',
     'nascido':'1962',
     'foto': 'https://static.wikia.nocookie.net/gta/images/7/7b/DevinWeston2-GTAV.png/revision/latest?cb=20160903005229&path-prefix=pt'
     },

     {'id': 27,
     'nome': 'Dave Norton',
     'negocios': 'FIB',
     'descricao': 'David Norton nasceu em um ano desconhecido mas provavelmente no fim dos anos 60, (devido a sua aparência) e se juntou ao FIB antes de 2004. Ele estava nas investigações sobre os roubos, dos criminosos Michael Townley, Trevor Philips e Brad Snider e possivelmente, outros.',
     'nacionalidade': 'Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/f/f5/Dave_N.png/revision/latest/scale-to-width-down/350?cb=20140814052658&path-prefix=pt'
     },

     {'id': 28,
     'nome': 'Steve Haines',
     'negocios': 'FIB e The Underbelly Of Paradise',
     'descricao': 'Steve nasceu em 1975 e se juntou a Federal Investigation Bureau (FIB) por volta de 1993. Nos anos seguintes ele foi um agente competente e habilidoso, se destacando entre os demais. Com tudo isso, ele se tornou um agente especial e começou a ser chefe de um trio do FIB, incluindo nele o Agente Andreas Sanchez, que foi um grande amigo de Steve por um tempo, e o agente Dave Norton. Eles eram encarregados de cuidar da Cidade de Los Santos e obedecer as ordens da agência do FIB de lá.',
     'nacionalidade': 'Americano',
     'nascido':'1975',
     'foto': 'https://static.wikia.nocookie.net/gta/images/c/c4/SteveHaines-GTAV.png/revision/latest?cb=20160828160322&path-prefix=pt'
     },

     {'id': 29,
     'nome': 'Lacey Jonas',
     'negocios': 'Atriz e cantora',
     'descricao': 'Lacey Jonas é muito famosa por seu trabalho em filmes para adolescentes.',
     'nacionalidade': 'Americana',
     'nascido':'1990',
     'foto': 'https://static.wikia.nocookie.net/gta/images/6/67/Lacy_Jonas.png/revision/latest?cb=20180129154941&path-prefix=pt'
     },

     {'id': 30,
     'nome': 'Simeon Yetarian',
     'negocios': 'Premium Deluxe Motorsport',
     'descricao': 'Simeon é um negociante automotivo de etnia armênia. Sua concessionária, no entanto, é um golpe; ele vende carros para pessoas que não podem pagar por eles e então os recupera por meio de esquemas de financiamento escusos e outros métodos duvidosos. No ar da liberdade de Los Santos, Simeon descobriu como usar sua etnia estrangeira como vantagem nos negócios, acusando quem é contra ele ou simplesmente não quer comprar o veículo de racista.',
     'nacionalidade': 'Armênio',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/c/cc/Simeon-GTA5.png/revision/latest?cb=20151104143949&path-prefix=pt'
     },

     {'id': 31,
     'nome': 'Molly Schultz',
     'negocios': 'Assessora',
     'descricao': 'Molly sempre foi ligada ao Direito e se especializou na área, esperando um contrato ela achou e aceitou um trabalho para o grande empreendedor Devin Weston, no qual ela dedicou a carreira assegurando de que seus investimentos e vontades fossem realizados de forma sucetíveis. Desde então, ela nunca abandonou o cliente, até conhecer um trio que estava trabalhando com Devin, Michael De Santa, Trevor Philips e Franklin Clinton.',
     'nacionalidade': 'Americana',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/3/32/MollySchultz.png/revision/latest?cb=20151224172649&path-prefix=pt'
     },

     {'id': 32,
     'nome': 'Martin Madrazo',
     'negocios': 'Cartel Madrazo',
     'descricao': 'É o líder de um cartel de drogas chamado Cartel Madrazo, ele é um poderoso e rico empresário estabelecido em Los Santos com sua esposa, Patricia Madrazo. Ele e a esposa, moram em sua fazenda intitulada La Fuente Blanca em Los Santos, e possui uma casa de alto padrão em Vinewood Hills.  Durante a história do GTA V, Michael De Santa destrói a mansão de Madrazo em Vinewood Hills, acreditando que a casa pertencia ao treinador de tênis de Amanda, Kyle Chavis, na missão Terapia de Casais. ',
     'nacionalidade': 'Mexicano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/a/a2/MartinMadrazo-GTAV.png/revision/latest?cb=20170124172940&path-prefix=pt'
     },

     {'id': 33,
     'nome': 'Tonya Wiggins',
     'negocios': 'Reboque de Los Santos',
     'descricao': 'Tonya nasceu e foi criada no Sul de Los Santos, com a filosofia de que "Gangue é família". Na infância seus amigos eram: Franklin Clinton, Tanisha Jackson, Lamar Davis e um garoto que era conhecido como JB. Na adolescência, Tonya começou a namorar JB, juntos eles começaram a mexer com drogas, alguns anos depois, ambos se viciaram em cocaína, crack e maconha. JB, tendo que sustentar a ele e  Tonya, conseguiu um emprego de Rebocador de Carros Roubados, mas com o tempo voltava a se viciar em drogas e isso o atrapalhava no trabalho. Tonya então chama Franklin Clinton, seu antigo amigo de infância para lhes ajudar em alguns reboques na missão Estranhos e Doidos.',
     'nacionalidade': 'Americana',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/e/ef/TonyaWiggins2-GTAV.png/revision/latest/scale-to-width-down/350?cb=20180628235559&path-prefix=pt'
     },

     {'id': 34,
     'nome': 'Isiah Friedlander',
     'negocios': 'Consultório Friedlander',
     'descricao': 'Em seu site oficial, Dr. Friedlander é dito ser um psicoterapeuta, personalidade da mídia, budista secular, e que deseja ser um de modelo barcos. Isiah recebeu o grau de bacharel em marketing pela Universidade de San Andreas, Los Santos em 1984 e doutorado em psicologia em 1986 a partir de uma instituição de ensino extinta desconhecida. Ele também tem viajado com freqüência na Ásia . Isiah tem sido amplamente elogiado por expor a cultura do narcisismo nas ganglands de San Andreas e também criticado por seu "uso excessivo de hífens". Ele é uma das maiores autoridades na área de Transtorno de Personalidade Sociopata e já tratou celebridades e criminosos. Isiah tornou-se um dos mais respeitados e requisitados terapeutas em Los Santos a partir de 2013.',
     'nacionalidade': 'Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/d/da/IsiahFriedlander.png/revision/latest?cb=20151224165727&path-prefix=pt'
     },

     {'id': 35,
     'nome': 'Patricia Madrazo',
     'negocios': 'Mulher do Martin Madrazo',
     'descricao': 'Pouco se sabe sobre Patricia, além de ser casada com Martin Madrazo, que a maltrata e a trai com uma mulher russa chamada Natalia Zverovna. Ela possui 57 anos de idade de acordo com Trevor. Ela usa um rosário em seu pescoço, o que implica que ela é uma católica romana.',
     'nacionalidade': 'Mexicana',
     'nascido':'1956',
     'foto': 'https://static.wikia.nocookie.net/gta/images/0/09/PatriciaMadrazo-GTAO-2020Portrait.png/revision/latest/scale-to-width-down/350?cb=20201224041339&path-prefix=pt'
     },

     {'id': 36,
     'nome': 'John Cranley',
     'negocios': 'Dublê (Anteriormente) e Candidato a governador',
     'descricao': 'Cranley tornou-se famoso na década de 1970 quando tinha o seu programa de TV chamado Stunt Double, e mais tarde viria a ser estrela em filmes. Cranley em seu programa advertia contra o uso de drogas e admitia ter tido problemas com drogas no passado. Ele foi preso pela VCPD, sob a acusação de vários crimes na época, embora sendo liberado mais tarde, afirmando que trabalhava como Dublê, e que tudo era autorizado pela polícia em Vice City.',
     'nacionalidade': 'Americano',
     'nascido':'1952',
     'foto': 'https://static.wikia.nocookie.net/gta/images/0/0b/JockCranley-GTAV.png/revision/latest/scale-to-width-down/350?cb=20170322160510&path-prefix=pt'
     },

     {'id': 37,
     'nome': 'Ron Jakowski',
     'negocios': 'Contador (anteriormente), CEO na Trevor Philips Enterprises e Locutor na Blaine County Radio Community Hour Hangares',
     'descricao': 'Ronald Jakowski nasceu possivelmente no Centro-Oeste dos Estados Unidos e trabalhou anteriormente como contador. Ele era casado antes de seu "melhor amigo" Trevor Philips entrar em sua vida. Trevor o convenceu de que sua esposa o estava retendo apenas na vida. Ron foi expulso por sua esposa e eles se divorciaram, com Ron profundamente endividado, porque ele ainda está pagando taxas de liquidação por ela. Ele então começou a ficar obcecado com as teorias da conspiração e começou a trabalhar para Trevor como CEO da Trevor Philips Enterprises. Em seu programa de rádio, Ron menciona que ele está trabalhando com a tecnologia de interferência de drones.',
     'nacionalidade': 'Polaco-Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/a/aa/Ron2017.png/revision/latest?cb=20191021131911&path-prefix=pt'
     },

     {'id': 38,
     'nome': 'Tao Cheng',
     'negocios': 'Cheng Family Holdings e Ex-proprietário do The Diamond Casino & Resort',
     'descricao': 'Nascido em Yangshan, China , Tao é o primogênito de Wei Cheng , o líder das Tríades de Los Santos. Tao fala principalmente em chinês mandarim . Embora ele fale e compreenda o inglês básico, geralmente é acompanhado por seu tradutor . Enquanto o ancião Cheng é implacável e facilmente capaz de retribuir qualquer um que se oponha a ele, Tao provou ser um sucessor da Tríade completamente inepto, exibindo os traços típicos de uma criança mimada. Constantemente se perdendo e sem qualquer senso de iniciativa durante as reuniões de negócios que ele deveria liderar, com o manuseio de seu tradutor. Apesar disso, seu pai se preocupa muito com o filho, apesar de seu comportamento, e nunca o repreende por ir a reuniões de negócios bêbado ou drogado.',
     'nacionalidade': 'Chinês',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gtawiki/images/8/88/TaoCheng2-GTAO-2019.png/revision/latest/scale-to-width-down/350?cb=20190826164936'
     },

     {'id': 39,
     'nome': 'Wei Cheng',
     'negocios': 'Dono da Gang Los Santos Triads.',
     'descricao': 'Cheng é um malicioso chinês nascido em Yangshan, que juntamente com o seu filho Tao Cheng, são donos da Gang Los Santos Triads, que lida principalmente com o contrabando de Armas e a fabricação de Metanfetamina. ele conta que em 2013 sua fabricação cresceu fortemente e ele procura expandir seu negocio em Blaine Country através de um grupo já funcionando lá, esse grupo seria o de Trevor, a Trevor Philips Enterprises.',
     'nacionalidade': 'Chinês',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/b/bd/WeiCheng2-GTAV.png/revision/latest?cb=20161003131720&path-prefix=pt'
     },

     {'id': 40,
     'nome': 'Floyd Hebert',
     'negocios': 'Empregado do Porto de Los Santos',
     'descricao': 'Floyd sempre foi um homem honesto e nunca quebrou a lei e as regras que lhe eram dadas. Quando mais velho, se casou com uma mulher chamada Debra e juntos, eles foram morar em um apartamento em Vespucci Beach, Los Santos, além de que Debra o ajudou a conseguir um emprego nas docas.',
     'nacionalidade': 'Americano',
     'nascido':'Desconhecido',
     'foto': 'https://static.wikia.nocookie.net/gta/images/c/cb/FloydHebert_ScoutingThePort.png/revision/latest/scale-to-width-down/350?cb=20180717143521&path-prefix=pt'
     },

]


@app.route('/personagens', methods=['GET'])
def obter_personagem():
    return jsonify(personagens)


@app.route('/personagem/<int:id>', methods=['GET'])
def obter_personagem_por_id(id):
    for personagem in personagens:
        if personagem.get('id') == id:
            return jsonify(personagem)

@app.route('/personagem/<nome>', methods=['GET'])
def obter_personagens_por_nome(nome):
    for personagem in personagens:
        if personagem.get('nome') == nome:
            return jsonify(personagem)

app.run(port=5000, host='localhost', debug=True)
