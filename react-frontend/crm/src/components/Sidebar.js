import React from 'react';
import { Link } from 'react-router-dom';
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
                    <Link to="/couriers" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Курьеры</Link>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <Link to="/clients" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Клиенты</Link>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <Link to="/orders" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Заказы</Link>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <Link to="/products" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Товары</Link>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <Link to="/delivery-routes" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Маршурты</Link>
                </li>
                <li style={{ margin: '15px 0' }}>
                    <Link to="/payments" style={{ textDecoration: 'none', color: '#333', fontWeight: 'bold' }}>Выплаты</Link>
                </li>
            </ul>
        </div>
    );
};

export default Sidebar;
