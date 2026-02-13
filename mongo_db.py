from pymongo import MongoClient

# INSTANCIACIÓN
def instanciar():
    # IMPORTANTE:
    # Si estás en Docker → usar mongo_bayeta
    # Si estás en local → usar localhost
    client = MongoClient("mongodb://mongo_bayeta:27017/")
    
    db = client["bayeta"]
    collection = db["frases_auspiciosas"]
    
    return collection


# INICIALIZACIÓN
def inicializar():
    collection = instanciar()
    
    # Solo insertamos si está vacía
    if collection.count_documents({}) == 0:
        with open("frases.txt", "r", encoding="utf-8") as f:
            frases = [{"frase": line.strip()} for line in f if line.strip()]
        
        collection.insert_many(frases)


# CONSULTA
def consultar(n_frases: int):
    collection = instanciar()
    
    frases_aleatorias = list(
        collection.aggregate([
            {"$sample": {"size": n_frases}}
        ])
    )
    
    return [frase["frase"] for frase in frases_aleatorias]
