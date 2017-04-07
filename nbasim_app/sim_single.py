import Game
import pandas as pd
import os, time
os.chdir(os.getcwd())
#simulation for a single match for N times

def sim(a_input,h_input,teams_df, c_home, lmda, N):
    t1=time.time()
    one_game=Game.Game(a_input,h_input,teams_df, c_home, lmda, N)
    rlt1, rlt2=one_game.sim_result(games)
    t2=time.time()-t1
    return rlt1, rlt2, t2
a_input='Los Angeles Lakers'
h_input='New Orleans Pelicans'
games=pd.read_csv('simulation_result.csv')
games=games.set_index('Unnamed: 0')
N=1
teams_df=pd.read_pickle('teams_df.pkl')
game_data=pd.read_pickle('game_data.pkl')
c_home=-game_data['diff'].mean()
lmda=game_data['sum'].mean()

a_out, h_out, time_cost=sim(a_input,h_input,teams_df, c_home, lmda, N)