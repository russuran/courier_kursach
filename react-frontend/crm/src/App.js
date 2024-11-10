import React from 'react';
import { Route, Routes } from 'react-router-dom';

import Sidebar from './components/Sidebar';

import DataTableComponent from './components/DataTableComponent';




const App = () => {
    return (
        <div style={{ display: 'flex', flexDirection: 'row' }}>
            <Sidebar style={{ flex: 1 }} />
            <div className="container" style={{ flex: 4, padding: '20px', backgroundColor: '#f4f4f4', marginLeft: '20px', border: '2px solid black', borderRadius: '16px' }}>
                <Routes>
                    {/* <Route path="/students" element={<DataTableComponent config={studentConfig} fitlers_to_pass={filters} />} /> */}
                    <Route path="/" element={<h1>Курьерский учет</h1>} />
                </Routes>
            </div>
        </div>
    );
};

export default App;