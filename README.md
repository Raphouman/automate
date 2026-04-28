L’objectif de ce programme est de créer un automate capable de vérifier que la syntaxe d’une phrase est correcte (en vue d’une
intégration ultérieure dans un correcteur grammatical par exemple ...). Une phrase est correcte (version
ultra simplifiée) si elle respecte le schéma :
Groupe nominal -> Groupe verbal -> Groupe nominal ->

On associe à chaque entrée une valeur numérique (0 = article ) et grâce à un (micro) dictionnaire
on précise le type de chaque mot ("le" = 0, "petit" = 1, "chat" = 2 ...).
— Il n’y a que 2 états de sortie :
— 9 = phrase correcte.
— 8 = phrase incorrecte.
""" 
