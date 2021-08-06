print('Start #################################################################');

db = db.getSiblingDB('Elo');
db.createUser(
  {
    user: 'elo',
    pwd: 'elo',
    roles: [{ role: 'readWrite', db: 'Elo' }],
  },
);
db.createCollection('DadosAtendimento');

print('END #################################################################');