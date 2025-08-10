const express = require('express');
const bodyParser = require('body-parser');
const sequelize = require('./db');
const orderRoutes = require('./routes/orderRoutes');

const app = express();
app.use(bodyParser.json());

app.use('/api/orders', orderRoutes);

sequelize.sync()
  .then(() => {
    console.log('Database synced');
    app.listen(5002, () => console.log('Order service running on port 5002'));
  })
  .catch(err => console.error('DB connection error:', err));
