import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Button } from 'primereact/button';
import { InputText } from 'primereact/inputtext';
import { Dialog } from 'primereact/dialog';
import { Toast } from 'primereact/toast';
import { Dropdown } from 'primereact/dropdown';
import { InputMask } from 'primereact/inputmask';


const Tables = ({ config }) => {
    const [data, setData] = useState([]);

    const [isModalOpenAdd, setIsModalOpenAdd] = useState(false);
    const [isModalOpenEdit, setIsModalOpenEdit] = useState(false);
    const [selectedItem, setSelectedItem] = useState(null);
    const [newItem, setNewItem] = useState(config.initialState);
    const toast = useRef(null);


    const filterMatchModeOptions = {
        text: [
            { label: 'Содержит', value: 'contains' },
            { label: 'Начинается с', value: 'startsWith' },
            { label: 'Заканчивается на', value: 'endsWith' },
            { label: 'Равно', value: 'equals' },
            { label: 'Не равно', value: 'notEquals' },
            { label: 'Не содержит', value: 'notContains' },
            { label: 'Без фильтра', value: 'noFilter' }
        ]
    };

    const filters = {
        Phone: { value: null, matchMode: 'contains' },
        CourierID: { value: null, matchMode: 'contains' },
        FullName: { value: null, matchMode: 'contains' },
        BirthDate: { value: null, matchMode: 'contains' },
        WorkExperience: { value: null, matchMode: 'contains' },
        TransportType: { value: null, matchMode: 'contains' },
        ClientID: { value: null, matchMode: 'contains' },
        Address: { value: null, matchMode: 'contains' },
        OrderID: { value: null, matchMode: 'contains' },
        OrderTime: { value: null, matchMode: 'contains' },
        DeliveryCost: { value: null, matchMode: 'contains' },
        PaymentStatus: { value: null, matchMode: 'contains' },
        Comment: { value: null, matchMode: 'contains' },
        ProductName: { value: null, matchMode: 'contains' },
        ProductType: { value: null, matchMode: 'contains' },
        Dimensions: { value: null, matchMode: 'contains' },
        RouteID: { value: null, matchMode: 'contains' },
        StartTime: { value: null, matchMode: 'contains' },
        EndTime: { value: null, matchMode: 'contains' },
        PaymentID: { value: null, matchMode: 'contains' },
        PaymentDate: { value: null, matchMode: 'contains' },
        ProductID: { value: null, matchMode: 'contains' },
        Weight: { value: null, matchMode: 'contains' },
        Quantity: { value: null, matchMode: 'contains' },
        OrderNumber: { value: null, matchMode: 'contains' },
        OrderCount: { value: null, matchMode: 'contains' },
    }

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(config.apiEndpoint, {});
                setData(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, [config.apiEndpoint]);

    const handleEdit = (item) => {
        setSelectedItem(item);
        setNewItem(item);
        setIsModalOpenEdit(true);
    };

    const handleDelete = async (item) => {
        try {
            setSelectedItem(item);
            const path = config.edit_key2 ? `${config.apiEndpoint}/${item[config.edit_key]}/${item[config.edit_key2]}` : `${config.apiEndpoint}/${item[config.edit_key]}`
            await axios.delete(path);
            
            setData((prevData) =>
                prevData.filter((prevItem) => prevItem[config.edit_key] !== item[config.edit_key])
            );
    
            toast.current.show({ severity: 'success', summary: 'Успех', detail: 'Запись удалена', life: 3000 });
        } catch (error) {
            toast.current.show({ severity: 'error', summary: 'Ошибка', detail: 'Не удалось удалить запись', life: 3000 });
        }
    };
    

    const handleUpdate = async () => {
        try {
            const path = config.edit_key2 ? `${config.apiEndpoint}/${selectedItem[config.edit_key]}/${selectedItem[config.edit_key2]}` : `${config.apiEndpoint}/${selectedItem[config.edit_key]}`
            await axios.put(path, newItem, {});

            setData((prevData) =>
                prevData.map((item) => (item[config.edit_key] === selectedItem[config.edit_key] ? newItem : item))
            );
            setIsModalOpenEdit(false);
            toast.current.show({ severity: 'success', summary: 'Успех', detail: 'Запись обновлена', life: 3000 });
        } catch (error) {
            const errorMessage = error.response && error.response.data && error.response.data.error
                ? error.response.data.error
                : 'Не удалось добавить запись';
    
            toast.current.show({ severity: 'error', summary: 'Ошибка', detail: errorMessage, life: 3000 });
        }
    };

    const handleAdd = async () => {
        try {
            const response = await axios.post(config.apiEndpoint, newItem, {});
            const response_add = await axios.get(config.apiEndpoint, {});
            setData(response_add.data);
            setIsModalOpenAdd(false);
            setNewItem(config.initialState);
            toast.current.show({ severity: 'success', summary: 'Выполнено', detail: 'Запись добавлена', life: 3000 });
        } catch (error) {
            console.error("Ошибка при добавлении записи:", error);
            

            const errorMessage = error.response && error.response.data && error.response.data.error
                ? error.response.data.error
                : 'Не удалось добавить запись';
    
            toast.current.show({ severity: 'error', summary: 'Не удалось выполнить', detail: errorMessage, life: 3000 });
        }
    };
    

    const header = (
        <div>
            <h2>{config.title}</h2>
            <Button label="Добавить" icon="pi pi-plus" onClick={() => [setIsModalOpenAdd(true), setNewItem(config.initialState)]} style={{ marginRight: '20px' }} />
        </div>
    );



    return (
        <>
            <Toast ref={toast} position="top-center"/>
            <DataTable
                style={{ padding: '4px', borderRadius: '16px', fontSize: '1rem' }}
                value={data}
                rows={100}
                header={header}
                filters={filters}
                filterDisplay="row"
                size='large'
                emptyMessage="Записей нет."
            >
                {config.columns.map((col) => (
                    <Column key={col.field} 
                            field={col.field} 
                            header={col.header}
                            filter
                            filterMatchModeOptions={filterMatchModeOptions.text}
                    />
                ))}
                <Column
                    header="Действия"
                    body={(rowData) => (
                        <div style={{ display: 'flex', gap: '20px'}}>
                        <Button
                            label="Редактировать"
                            onClick={() => handleEdit(rowData)}
                        />
                        <Button
                            label="Удалить"
                            onClick={() => handleDelete(rowData)}
                        />
                        </div>
                    )}
                    style={{ minWidth: '8rem' }}
                />
            </DataTable>

            <Dialog header="Добавить Запись" visible={isModalOpenAdd} onHide={() => setIsModalOpenAdd(false)}>
            <div>
                {config.columns.map((col) => (
                    <div 
                        key={col.field} 
                        style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginTop: '20px', gap: '20px' }}
                    >
                        <label htmlFor={col.field}>{col.header}</label>
                        {col.dropdown ? (
                            col.dropdown !== undefined ? (
                                <Dropdown 
                                    id={col.field}
                                    style={{ width: '236px' }}
                                    value={newItem[col.field]} 
                                    onChange={(e) => setNewItem({ ...newItem, [col.field]: e.target.value })}
                                    options={col.dropdown} 
                                    checkmark={true}  
                                    highlightOnSelect={false} 
                                    required={col.required}
                                />
                            ) : (
                                <div>...</div>
                            )
                        ) : (
                            col.mask ? (
                                <InputMask
                                    id={col.field}
                                    style={{ width: '236px' }}
                                    value={newItem[col.field]}
                                    onChange={(e) => setNewItem({ ...newItem, [col.field]: e.target.value })}
                                    disabled={col.disabled}
                                    mask={col.mask}
                                    required={col.required}
                                />
                            ) : (
                                <InputText
                                    id={col.field}
                                    style={{ width: '236px' }}
                                    value={newItem[col.field]}
                                    onChange={(e) => setNewItem({ ...newItem, [col.field]: e.target.value })}
                                    disabled={col.disabled}
                                    required={col.required}
                                />
                            )
                        )}
                    </div>
                ))}
                </div>
                <div style={{ display: 'flex', justifyContent: 'right', marginTop: '20px', gap: '20px' }}>
                    <Button label="Добавить" onClick={handleAdd} />
                    <Button label="Отмена" onClick={() => setIsModalOpenAdd(false)} className="p-button-secondary" />
                </div>
            </Dialog>

            <Dialog header="Редактировать Запись" visible={isModalOpenEdit} onHide={() => setIsModalOpenEdit(false)}>
            <div>
                {config.columns.map((col) => (
                    <div 
                        key={col.field} 
                        style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginTop: '20px', gap: '20px' }}
                    >
                        <label htmlFor={col.field}>{col.header}</label>
                        {col.dropdown ? (
                            col.dropdown ? (
                                <Dropdown 
                                    id={col.field}
                                    style={{ width: '236px' }}
                                    value={newItem[col.field]} 
                                    onChange={(e) => setNewItem({ ...newItem, [col.field]: e.target.value })}
                                    options={col.dropdown} 
                                    checkmark={true}  
                                    highlightOnSelect={false} 
                                />
                            ) : (
                                <div>...</div>
                            )
                        ) : (
                            col.mask ? ( // Проверяем, существует ли col.mask
                                <InputMask
                                    id={col.field}
                                    style={{ width: '236px' }}
                                    value={newItem[col.field]}
                                    onChange={(e) => setNewItem({ ...newItem, [col.field]: e.target.value })}
                                    disabled={col.disabled}
                                    mask={col.mask} // Устанавливаем маску
                                />
                            ) : (
                                <InputText
                                    id={col.field}
                                    style={{ width: '236px' }}
                                    value={newItem[col.field]}
                                    onChange={(e) => setNewItem({ ...newItem, [col.field]: e.target.value })}
                                    disabled={col.disabled}
                                />
                            )
                        )}
                    </div>
                    ))}
                </div>
                <div style={{ display: 'flex', justifyContent: 'right', marginTop: '20px', gap: '20px' }}>
                    <Button label="Сохранить" icon="pi pi-check" onClick={handleUpdate} />
                    <Button label="Отмена" icon="pi pi-times" onClick={() => setIsModalOpenEdit(false)} className="p-button-secondary" />
                </div>
            </Dialog>
        </>
    );
};

export default Tables;

