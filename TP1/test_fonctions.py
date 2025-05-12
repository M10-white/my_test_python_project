from fonctions import calculer_ttc, verifier_mot_de_passe, convertir_date

def test_calculer_ttc_normal():
    assert calculer_ttc(100, 0.2) == 120

def test_calculer_ttc_zero():
    assert calculer_ttc(0, 0.2) == 0

def test_verifier_mot_de_passe_valid():
    assert verifier_mot_de_passe("MotDePasse1") == True

def test_verifier_mot_de_passe_invalid():
    assert verifier_mot_de_passe("motdepasse") == False

def test_convertir_date():
    assert convertir_date("25/12/2024") == "2024-12-25"
    
def test_verifier_mot_de_passe_vide():
    """Test avec un mot de passe vide"""
    assert verifier_mot_de_passe("") == False
