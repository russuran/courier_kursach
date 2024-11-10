import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import axios from 'axios';

import 'primereact/resources/primereact.min.css';
import  'primereact/resources/themes/bootstrap4-light-blue/theme.css'

import Sidebar from './components/Sidebar';
import Tables from './components/Tables';





const App = () => {
  const [couriers, setCouriers] = useState([]);
  const [client, setClients] = useState([]);
  const [order, setOrders] = useState([]);
  const [product, setProducts] = useState([]);
  const [deliver, setDelivers] = useState([]);

  const fetchData = async () => {
    try {
      const response1 = await axios.get('http://127.0.0.1:5000/couriers_list');
      setCouriers(response1.data);

      const response2 = await axios.get('http://127.0.0.1:5000/clients_list');
      setClients(response2.data);

      const response3 = await axios.get('http://127.0.0.1:5000/orders_list');
      setOrders(response3.data);

      const response4 = await axios.get('http://127.0.0.1:5000/products_list');
      setProducts(response4.data);

      const response5 = await axios.get('http://127.0.0.1:5000/delivers_list');
      setDelivers(response5.data);

    } catch (error) {
      console.error('Ошибка при получении курьеров:', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);


  const courier = {
    apiEndpoint: 'http://127.0.0.1:5000/couriers',
    columns: [
        { field: 'FullName', header: 'ФИО' },
        { field: 'Phone', header: 'Номер Телефона', mask: "7(999)999-99-99", placeholder: "7(999)999-99-99" },
        { field: 'BirthDate', header: 'День Рождения', mask: "99/99/9999", placeholder: "99/99/9999", slotChar: "дд/мм/гггг" },
        { field: 'WorkExperience', header: 'Опыт работ' },
        { field: 'TransportType', header: 'Транспорт' },
  
    ],
    title: 'Курьеры',
    initialState: {
        CourierID: null,
        FullName: null,
        Phone: null,
        BirthDate: null,
        WorkExperience: null,
        TransportType: null,
    },
    edit_key: 'CourierID'
  };
  
  const clients = {
    apiEndpoint: 'http://127.0.0.1:5000/clients',
    columns: [
        { field: 'FullName', header: 'ФИО' },
        { field: 'Phone', header: 'Номер Телефона', mask: "7(999)999-99-99", placeholder: "7(999)999-99-99" },
        { field: 'Address', header: 'Адрес' },
    ],
    title: 'Клиенты',
    initialState: {
        ClientID: null,
        FullName: null,
        Phone: null,
        Address: null,
    },
    edit_key: 'ClientID'
  };
  
  const orders = {
    apiEndpoint: 'http://127.0.0.1:5000/orders',
    columns: [
        { field: 'ClientID', header: 'Клиент', dropdown: client },
        { field: 'OrderTime', header: 'Время Заказа', mask: "99:99", placeholder: "12:12" },
        { field: 'DeliveryCost', header: 'Стоимость Доставки' },
        { field: 'PaymentStatus', header: 'Статус Платежа' },
        { field: 'Comment', header: 'Комментарий' },
    ],
    title: 'Заказы',
    initialState: {
        OrderID: null,
        ClientID: null,
        OrderTime: null,
        DeliveryCost: 0,
        PaymentStatus: null,
        Comment: null,
    },
    edit_key: 'OrderID'
  };
  
  const products = {
    apiEndpoint: 'http://127.0.0.1:5000/products',
    columns: [
        { field: 'ProductName', header: 'Наименование' },
        { field: 'ProductType', header: 'Тип' },
        { field: 'Weight', header: 'Вес' },
        { field: 'Dimensions', header: 'Размер' },
    ],
    title: 'Товары',
    initialState: {
        ProductID: null,
        ProductName: null,
        ProductType: null,
        Weight: null,
        Dimensions: null,
    },
    edit_key: 'ProductID'
  };
  
  
  const delivery = {
    apiEndpoint: 'http://127.0.0.1:5000/delivery_routes',
    columns: [
        { field: 'CourierID', header: 'Курьер', dropdown: couriers  },
        { field: 'StartTime', header: 'Время Начала', mask: "99:99", placeholder: "чч:мм" },
        { field: 'EndTime', header: 'Время Конца', mask: "99:99", placeholder: "чч:мм" },
        { field: 'OrderCount', header: 'Количество Заказов' },
    ],
    title: 'Маршруты Доставки',
    initialState: {
        RouteID: null,
        CourierID: null,
        StartTime: null,
        EndTime: null,
        OrderCount: null,
    },
    edit_key: 'RouteID'
  };
  
  const payments = {
    apiEndpoint: 'http://127.0.0.1:5000/payments',
    columns: [
        { field: 'OrderID', header: 'Заказ', dropdown: order },
        { field: 'PaymentDate', header: 'Дата Платежа', mask: "99/99/9999", placeholder: "99/99/9999", slotChar: "дд/мм/гггг" },
    ],
    title: 'Платежи',
    initialState: {
        PaymentID: null,
        OrderID: null,
        PaymentDate: null,
    },
    edit_key: 'PaymentID'
  };

  const order_content = {
    apiEndpoint: 'http://127.0.0.1:5000/order_contents',
    columns: [
        { field: 'OrderID', header: 'Заказ', dropdown: order },
        { field: 'ProductID', header: 'Товар', dropdown: product },
        { field: 'Quantity', header: 'Количество' },
    ],
    title: 'Содержимое Заказов',
    initialState: {
        OrderID: null,
        ProductID: null,
        Quantity: null,
    },
    edit_key: 'OrderID',
    edit_key2: 'ProductID'
  };

  const delivery_content = {
    apiEndpoint: 'http://127.0.0.1:5000/route_contents',
    columns: [
        { field: 'RouteID', header: 'Маршрут', dropdown: deliver },
        { field: 'OrderID', header: 'Заказ', dropdown: order },
        { field: 'OrderNumber', header: 'Порядковый номер'}
    ],
    title: 'Содержимое Маршрутов',
    initialState: {
        RouteID: null,
        OrderID: null,
        OrderNumber: null,
    },
    edit_key: 'RouteID',
    edit_key2: 'OrderID'
  }

    return (
        <div style={{ display: 'flex', flexDirection: 'row' }}>
            <Sidebar style={{ flex: 1 }} />
            <div className="container" style={{ flex: 4, padding: '20px', backgroundColor: '#f4f4f4', marginLeft: '20px', border: '2px solid black', borderRadius: '16px' }}>
                <Routes>
                    <Route path="/couriers" element={<Tables config={courier}  />} />
                    <Route path="/clients" element={<Tables config={clients}  />} />
                    <Route path="/orders" element={<Tables config={orders}  />} />
                    <Route path="/products" element={<Tables config={products}  />} />
                    <Route path="/delivery-routes" element={<Tables config={delivery}  />} />
                    <Route path="/payments" element={<Tables config={payments}  />} />
                    <Route path="/order-content" element={<Tables config={order_content}  />} />
                    <Route path="/delivery-content" element={<Tables config={delivery_content}  />} />
                    <Route path="/" element={<h1>Курьерский учет</h1>} />
                </Routes>
            </div>
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
        <App />
    </BrowserRouter>
  </React.StrictMode>
);
