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
