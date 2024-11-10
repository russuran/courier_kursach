import React from 'react';
// import './Sidebar.css';

const Sidebar = () => {
    return (
        <div style={{ width: '300px',
                      height: '100vh',
                      backgroundColor: '#f4f4f4',
                      padding: '20px', 
                      border: '2px solid black',
                      borderRadius: '16px',
                      fontSize: '20px'
                    }}
        >
            <h2 style={{ textAlign: 'center' }}>Меню</h2>
            <ul style={{
                        listStyleType: 'none',
                        padding: 0
                      }}
            >
                <li style={{ margin: '15px 0' }}> 
                    <a href="/couriers" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Курьеры</a>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <a href="/clients" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Клиенты</a>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <a href="/orders" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Заказы</a>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <a href="/order-content" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Содержание Заказов</a>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <a href="/products" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Товары</a>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <a href="/delivery-routes" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Маршурты</a>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <a href="/delivery-content" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Составление Маршрутов</a>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <a href="/payments" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Платежи</a>
                </li>
            </ul>
        </div>
    );
};

export default Sidebar;
