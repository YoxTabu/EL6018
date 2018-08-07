import unittest
import os.path
import sqlite3

import soft1

class Test(unittest.TestCase):
    
    def test_crear_DB(self):
        BDFILE = 'DB.sqlite'
        TABLA = 'megatabla'
        CAMPO = 'texto_random'
        TIPO = 'VARCHAR(200)'
        soft1.crear_BD(BDFILE,TABLA,CAMPO,TIPO)
        self.assertTrue(os.path.isfile(BDFILE))

    def test_BD_table(self):
        BDFILE = 'DB.sqlite'
        TABLA = 'megatabla'
        CAMPO = 'texto_random'
        TIPO = 'VARCHAR(200)'  

        conn = sqlite3.connect(BDFILE)
        c = conn.cursor()
        try:
            c.execute('SELECT count(*) FROM sqlite_master WHERE type = \'table\' AND name = \'{tn}\''.\
                              format(tn=TABLA))
        except:
            self.assertTrue(1==0)
        conn.commit()
        conn.close()   
        
        
    def test_IO_BD(self):
        BDFILE = 'DB.sqlite'
        TABLA = 'megatabla'
        CAMPO = 'texto_random'
        txt = 'new entry'
        soft1.escribir_DB(txt,BDFILE,TABLA,CAMPO)
        a=soft1.leer_BD(BDFILE,TABLA)
        self.assertTrue(txt==a[-1][0])

if __name__ == '__main__':
    unittest.main()
