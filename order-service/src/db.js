const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('orderdb', 'orderuser', 'orderpass', {
  host: 'localhost',
  dialect: 'postgres'
});

module.exports = sequelize;
