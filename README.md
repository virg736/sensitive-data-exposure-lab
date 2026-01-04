# Sensitive Data Exposure - Environnement Controlé

# Exposition de données sensibles  
*(Parrot OS ↔ Debian / Apache)*

##  Objectif

Ce projet démontre, dans un **environnement strictement contrôlé**, comment des données sensibles peuvent être **exposées involontairement** via une page web, puis **détectées automatiquement** à l’aide d’un script Python utilisant des **expressions régulières**.

Toutes les données utilisées sont **fictives** et destinées **uniquement à la démonstration pédagogique**.

--- 

##  Environnement

- **Client** : Parrot OS  
- **Serveur** : Debian GNU/Linux + Apache2  
- **Réseau** : privé / isolé (`192.168.x.x`)  
- **Hyperviseur** : VirtualBox  

---

## Étape 1 - Vérification de la connectivité réseau

Avant toute analyse applicative, la connectivité réseau entre les machines virtuelles est vérifiée à l’aide de requêtes ICMP.

### Parrot → Debian
ping 192.168.100.10

Debian → Parrot
ping 192.168.100.20

✅ Résultat attendu : communication réseau fonctionnelle.

---

## 🌐 Étape 2 - Vérification du serveur web (Debian)

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

🔍 Étape 4 - Test local de la page (Debian)

On vérifie que la page est correctement servie par Apache côté serveur.

`curl http://127.0.0.1/sensitive_demo.html`

➡ La page est bien servie localement.

---

## 🌍 Étape 5 — Accès distant depuis Parrot OS

On accède à la page exposée depuis la machine Parrot via le réseau interne.

Commande utilisée :  
`curl http://192.168.100.10/sensitive_demo.html`

➡ **Les données exposées sont accessibles depuis le réseau interne.**

---

## 🐍 Étape 6 - Création du script de détection (Parrot)

Un script Python minimaliste est créé afin d’analyser le contenu de la page web.

nano sensitive_mini.py

---
