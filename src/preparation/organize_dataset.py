from pathlib import Path
import shutil

RAWDATA_PATH = Path('data/raw/')

def org_demos():
    
    DS_PATH = RAWDATA_PATH / 'DEMOS_Emotions'
    shutil.move(RAWDATA_PATH / 'DEMoS/NEU', DS_PATH)
    
    RAW_DS_PATH = RAWDATA_PATH / 'DEMoS/DEMOS'
    
    for subdir, dirs, files in os.walk(RAW_DS_PATH):
        for file in files:
            emotion = file[8:11] # if DEMoS
            if emotion == 'neu': # neutral
                path_paste = DS_PATH / '0 - Neutral/'
            elif emotion == 'gio': # happy 
                path_paste = DS_PATH / '1 - Happy/'
            elif emotion == 'tri': # sadness
                path_paste = DS_PATH / '2 - Sad/'
            elif emotion == 'rab': # anger
                path_paste = DS_PATH / '3 - Anger/'
            elif emotion == 'pau' or emotion == 'ans': # fear 
                path_paste = DS_PATH / '4 - Fear/'
            elif emotion == 'dis': # disgust 
                path_paste = DS_PATH / '5 - Disgust/'
            elif emotion == 'sor': # surprise
                path_paste = DS_PATH / '6 - Surprise/'
            elif emotion == 'col': # guilt
                path_paste = DS_PATH / '7 - Guilt/'      

            # Criar caminho caso não exista
            if not os.path.exists(DS_PATH):
                os.makedirs(DS_PATH)

            # Colar arquivos
            shutil.move(RAW_DS_PATH / file, DS_PATH / file)

    # Delete empty folders
    shutil.rmtree(RAWDATA_PATH / 'DEMoS')