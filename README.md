<h1 align="center">Sensitive Data Exposure - Environment Controlé</h1>

<p align="center">
Exposition de données sensibles<br>
(Parrot OS ↔ Debian / Apache)
</p>


# Objectif

Ce projet démontre, dans un **environnement strictement contrôlé**, comment des données sensibles peuvent être **exposées involontairement** via une page web, puis **détectées automatiquement** à l’aide d’un script Python utilisant des **expressions régulières**.

Toutes les données utilisées sont **fictives** et destinées **uniquement à la démonstration pédagogique**.

--- 

# Environnement

- **Client** : Parrot OS  
- **Serveur** : Debian GNU/Linux + Apache2  
- **Réseau** : privé / isolé (`192.168.x.x`)  
- **Hyperviseur** : VirtualBox  

---

📄 Étape 1 - Vérification de la connectivité réseau

Avant toute analyse applicative, la connectivité réseau entre les machines virtuelles est vérifiée à l’aide de requêtes ICMP.

### Parrot → Debian
ping 192.168.100.10

Debian → Parrot
ping 192.168.100.20

✅ Résultat attendu : communication réseau fonctionnelle.

---

 📄 Étape 2 - Vérification du serveur web (Debian)

On vérifie que le service Apache est actif sur la machine cible.

sudo systemctl status apache2

➡ Apache est actif et prêt à servir du contenu.

---

📄 Étape 3 - Création de la page HTML exposée (Debian)   

Une page HTML de démonstration est créée afin de simuler une exposition de données sensibles.   

sudo nano /var/www/html/sensitive_demo.html   

La page contient volontairement les éléments suivants (données factices) :   
	•	adresse e-mail fictive   
	•	mot de passe de démonstration   
	•	clé AWS factice  
	•	token GitHub factice    
	•	numéro de carte bancaire de test      

Recharge du service Apache :    

sudo systemctl reload apache2   

---

📄 Étape 4 - Test local de la page (Debian)

On vérifie que la page est correctement servie par Apache côté serveur.

`curl http://127.0.0.1/sensitive_demo.html`

➡ La page est bien servie localement.

---

📄 Étape 5 - Accès distant depuis Parrot OS

On accède à la page exposée depuis la machine Parrot via le réseau interne.

Commande utilisée :  
`curl http://192.168.100.10/sensitive_demo.html`

➡ **Les données exposées sont accessibles depuis le réseau interne.**

---

📄 Étape 6 - Création du script de détection (Parrot)   

Un script Python minimaliste est créé afin d’analyser le contenu de la page web.   

nano sensitive_mini.py   

Fonctions du script :   
	•	téléchargement du contenu HTML    
	•	détection via expressions régulières (regex)    
	•	affichage structuré des résultats   

---

📂 Étape 7 - Vérification du script   

On vérifie la présence du script dans le répertoire courant.   

ls   

▶️ Étape 8 - Exécution du scan automatisé   

Le script est exécuté contre l’URL de la page exposée.   

Commande utilisée :   Commande utilisée :  
`python3 sensitive_mini.py (http://192.168.100.10/sensitive_demo.html)`

Résultats détectés :   
	•	adresse e-mail   
	•	clé AWS (fake)   
	•	token GitHub (fake)   
	•	numéro de carte bancaire de test   

---


##  Analyse sécurité (contexte réel)

Dans un environnement réel, ce type d’exposition peut provenir :
- d’une page de test oubliée  
- d’un fichier de debug  
- d’une API trop verbeuse  
- de secrets exposés côté frontend  

⚠️ **Aucune exploitation avancée n’est nécessaire** :  
il suffit d’accéder à la ressource exposée et d’en analyser le contenu.

---

##  Bonnes pratiques recommandées

- supprimer immédiatement le contenu exposé  
- révoquer et faire tourner les secrets  
- utiliser des variables d’environnement  
- mettre en place des scans de secrets automatisés (CI/CD)  
- réaliser des audits de sécurité réguliers  

---

## 🔒 Sécurité de l’environnement de test

- réseau isolé  
- aucune exposition Internet  
- service Apache arrêté après la démonstration  
- données strictement factices  

---

## ⚠️ Avertissement

Projet strictement éducatif.  
Aucune donnée réelle n’est utilisée.  
Aucun système tiers n’a été ciblé.

---

## ✅ Résultat final

✔ Projet publiable sur GitHub  
✔ Lisible par recruteur ou jury  
✔ Orientation **défensive et pédagogique**

