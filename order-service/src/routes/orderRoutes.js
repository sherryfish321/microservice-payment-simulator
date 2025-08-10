const express = require('express');
const router = express.Router();
const Order = require('../models/order');

// 健康檢查
router.get('/health', (req, res) => {
  res.json({ status: 'Order service is healthy' });
});

// 新增訂單
router.post('/', async (req, res) => {
  try {
    const order = await Order.create(req.body);
    res.status(201).json(order);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 查詢訂單
router.get('/:id', async (req, res) => {
  try {
    const order = await Order.findByPk(req.params.id);
    if (order) {
      res.json(order);
    } else {
      res.status(404).json({ error: 'Order not found' });
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
